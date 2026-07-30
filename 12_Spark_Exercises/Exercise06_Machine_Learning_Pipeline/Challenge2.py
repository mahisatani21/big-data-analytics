from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# -----------------------------------
# Create Spark Session
# -----------------------------------

spark = SparkSession.builder \
    .appName("Customer Churn Prediction") \
    .getOrCreate()

# -----------------------------------
# Sample Dataset
# -----------------------------------

data = spark.createDataFrame([
    (25, 35000, 5, 20, 0),
    (30, 45000, 8, 15, 0),
    (35, 60000, 12, 30, 1),
    (40, 70000, 15, 28, 1),
    (45, 85000, 20, 40, 1),
    (28, 40000, 6, 18, 0),
    (23, 30000, 2, 10, 0),
    (50, 90000, 25, 35, 1),
    (38, 65000, 13, 26, 1),
    (31, 48000, 9, 19, 0)
], [
    "age",
    "income",
    "purchase_history",
    "website_visits",
    "label"
])

print("\nCustomer Data")
data.show()

# -----------------------------------
# Feature Vector
# -----------------------------------

assembler = VectorAssembler(
    inputCols=[
        "age",
        "income",
        "purchase_history",
        "website_visits"
    ],
    outputCol="features"
)

dataset = assembler.transform(data)

# -----------------------------------
# Train/Test Split
# -----------------------------------

train, test = dataset.randomSplit([0.8, 0.2], seed=42)

# -----------------------------------
# Logistic Regression
# -----------------------------------

lr = LogisticRegression(
    featuresCol="features",
    labelCol="label"
)

model = lr.fit(train)

predictions = model.transform(test)

print("\nPredictions")

predictions.select(
    "label",
    "prediction",
    "probability"
).show(truncate=False)

# -----------------------------------
# Accuracy
# -----------------------------------

evaluator = BinaryClassificationEvaluator(
    labelCol="label"
)

accuracy = evaluator.evaluate(predictions)

print(f"\nModel Score : {accuracy:.4f}")

spark.stop()
