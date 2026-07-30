from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# -----------------------------------
# Create Spark Session
# -----------------------------------

spark = SparkSession.builder \
    .appName("ALS Recommendation System") \
    .getOrCreate()

# -----------------------------------
# Sample User Ratings
# -----------------------------------

ratings = spark.createDataFrame([
    (1, 101, 5.0),
    (1, 102, 3.0),
    (1, 103, 4.0),
    (2, 101, 4.0),
    (2, 103, 5.0),
    (3, 101, 2.0),
    (3, 102, 5.0),
    (3, 104, 4.0),
    (4, 102, 4.0),
    (4, 103, 3.0),
    (4, 104, 5.0)
], ["userId", "productId", "rating"])

print("\nRatings Dataset")
ratings.show()

# -----------------------------------
# Train/Test Split
# -----------------------------------

train, test = ratings.randomSplit([0.8, 0.2], seed=42)

# -----------------------------------
# ALS Model
# -----------------------------------

als = ALS(
    userCol="userId",
    itemCol="productId",
    ratingCol="rating",
    coldStartStrategy="drop",
    nonnegative=True,
    rank=10,
    maxIter=10,
    regParam=0.1
)

model = als.fit(train)

# -----------------------------------
# Predictions
# -----------------------------------

predictions = model.transform(test)

print("\nPredictions")
predictions.show()

# -----------------------------------
# RMSE
# -----------------------------------

evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating",
    predictionCol="prediction"
)

rmse = evaluator.evaluate(predictions)

print(f"\nRMSE : {rmse:.2f}")

# -----------------------------------
# Recommendations
# -----------------------------------

print("\nTop 3 Recommendations")

recommendations = model.recommendForAllUsers(3)

recommendations.show(truncate=False)

spark.stop()
