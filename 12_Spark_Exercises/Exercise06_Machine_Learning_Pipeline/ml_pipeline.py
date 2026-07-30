from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import (
    VectorAssembler,
    StandardScaler,
    StringIndexer
)
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

# -----------------------------------
# Create Spark Session
# -----------------------------------

spark = SparkSession.builder \
    .appName("Machine Learning Pipeline") \
    .getOrCreate()

# -----------------------------------
# Read Dataset
# -----------------------------------

df = spark.read.csv(
    "customer_data.csv",
    header=True,
    inferSchema=True
)

print("\nCustomer Dataset")
df.show()

# -----------------------------------
# Feature Engineering
# -----------------------------------

feature_cols = [
    "age",
    "income",
    "purchase_history",
    "website_visits"
]

string_indexer = StringIndexer(
    inputCol="category",
    outputCol="category_index"
)

assembler = VectorAssembler(
    inputCols=feature_cols + ["category_index"],
    outputCol="features_vector"
)

scaler = StandardScaler(
    inputCol="features_vector",
    outputCol="scaled_features",
    withStd=True,
    withMean=True
)

# -----------------------------------
# Random Forest Model
# -----------------------------------

rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="scaled_features",
    numTrees=100,
    seed=42
)

# -----------------------------------
# Pipeline
# -----------------------------------

pipeline = Pipeline(
    stages=[
        string_indexer,
        assembler,
        scaler,
        rf
    ]
)

# -----------------------------------
# Train/Test Split
# -----------------------------------

train_data, test_data = df.randomSplit(
    [0.8, 0.2],
    seed=42
)

# -----------------------------------
# Hyperparameter Tuning
# -----------------------------------

param_grid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [50, 100, 200]) \
    .addGrid(rf.maxDepth, [5, 10, 20]) \
    .build()

evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

cross_validator = CrossValidator(
    estimator=pipeline,
    estimatorParamMaps=param_grid,
    evaluator=evaluator,
    numFolds=3,
    seed=42
)

# -----------------------------------
# Train Model
# -----------------------------------

cv_model = cross_validator.fit(train_data)

# -----------------------------------
# Predictions
# -----------------------------------

predictions = cv_model.transform(test_data)

print("\nPredictions")
predictions.select(
    "label",
    "prediction",
    "probability"
).show(truncate=False)

# -----------------------------------
# Accuracy
# -----------------------------------

accuracy = evaluator.evaluate(predictions)

print(f"\nModel Accuracy: {accuracy:.4f}")

spark.stop()
