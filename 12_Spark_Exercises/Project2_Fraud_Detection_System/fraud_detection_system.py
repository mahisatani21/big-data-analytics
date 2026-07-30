from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# -----------------------------------------
# Create Spark Session
# -----------------------------------------
spark = SparkSession.builder \
    .appName("Fraud Detection System") \
    .getOrCreate()

# -----------------------------------------
# Sample Transaction Data
# -----------------------------------------
data = [
    (1, 101, "2024-01-01 10:00:00", 120.0),
    (2, 101, "2024-01-01 10:10:00", 850.0),
    (3, 102, "2024-01-01 11:00:00", 1500.0),
    (4, 101, "2024-01-01 11:20:00", 600.0),
    (5, 102, "2024-01-01 12:15:00", 200.0),
    (6, 103, "2024-01-01 13:00:00", 2500.0)
]

columns = [
    "transaction_id",
    "user_id",
    "timestamp",
    "amount"
]

transactions = spark.createDataFrame(data, columns)

transactions = transactions.withColumn(
    "timestamp",
    to_timestamp(col("timestamp"))
)

# -----------------------------------------
# Fraud Detection System Class
# -----------------------------------------
class FraudDetectionSystem:

    def __init__(self, spark):
        self.spark = spark
        self.model = None

    # -------------------------------------
    # Feature Engineering
    # -------------------------------------
    def feature_engineering(self, transactions):

        features = transactions.withColumn(
            "hour_of_day",
            hour("timestamp")
        ).withColumn(
            "day_of_week",
            dayofweek("timestamp")
        ).withColumn(
            "amount_category",
            when(col("amount") > 1000, "high")
            .when(col("amount") > 500, "medium")
            .otherwise("low")
        )

        window_spec = Window.partitionBy("user_id").orderBy("timestamp")

        features = features.withColumn(
            "rolling_avg_5",
            avg("amount").over(
                window_spec.rowsBetween(-5, Window.currentRow)
            )
        ).withColumn(
            "transaction_count_1h",
            count("transaction_id").over(
                window_spec.rowsBetween(-60, Window.currentRow)
            )
        )

        return features

    # -------------------------------------
    # Train Model
    # -------------------------------------
    def train_model(self, features):

        training_data = features.withColumn(
            "label",
            when(col("amount") > 1000, 1).otherwise(0)
        )

        assembler = VectorAssembler(
            inputCols=[
                "amount",
                "hour_of_day",
                "day_of_week",
                "rolling_avg_5",
                "transaction_count_1h"
            ],
            outputCol="features"
        )

        dataset = assembler.transform(training_data)

        train, test = dataset.randomSplit([0.8, 0.2], seed=42)

        rf = RandomForestClassifier(
            featuresCol="features",
            labelCol="label",
            numTrees=20
        )

        self.model = rf.fit(train)

        predictions = self.model.transform(test)

        return predictions, features

    # -------------------------------------
    # Detect Anomalies
    # -------------------------------------
    def detect_anomalies(self, predictions):

        anomalies = predictions.filter(col("prediction") == 1)

        return anomalies


# -----------------------------------------
# Main Program
# -----------------------------------------

fraud = FraudDetectionSystem(spark)

# Feature Engineering
features = fraud.feature_engineering(transactions)

print("\n========== Feature Engineered Data ==========")
features.show(truncate=False)

# Train Model
predictions, features = fraud.train_model(features)

print("\n========== Fraud Detection Predictions ==========")
predictions.select(
    "transaction_id",
    "user_id",
    "amount",
    "prediction",
    "probability"
).show(truncate=False)

# Detect Anomalies
anomalies = fraud.detect_anomalies(predictions)

print("\n========== Potential Fraud Transactions ==========")
anomalies.select(
    "transaction_id",
    "user_id",
    "amount"
).show()

# -----------------------------------------
# Challenge Analysis
# -----------------------------------------

print("\n========== Additional Fraud Analysis ==========")

# High-value transactions
high_value = features.filter(col("amount") > 1000)

print("\nHigh Value Transactions")
high_value.select(
    "transaction_id",
    "user_id",
    "amount"
).show()

# Frequent users
frequent_users = features.groupBy("user_id") \
    .agg(count("transaction_id").alias("transaction_count")) \
    .filter(col("transaction_count") >= 2)

print("\nFrequent Users")
frequent_users.show()

# Average transaction amount
avg_amount = features.groupBy("user_id") \
    .agg(avg("amount").alias("average_amount"))

print("\nAverage Transaction Amount")
avg_amount.show()

# High spending users
high_spenders = avg_amount.filter(
    col("average_amount") > 1000
)

print("\nHigh Spending Users")
high_spenders.show()

print("\nFraud Detection System Executed Successfully.")

# -----------------------------------------
# Stop Spark
# -----------------------------------------
spark.stop()
