from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# ---------------------------------------
# Create Spark Session
# ---------------------------------------

spark = SparkSession.builder \
    .appName("Feature Importance Analysis") \
    .getOrCreate()

# ---------------------------------------
# Sample Dataset
# ---------------------------------------

data = spark.createDataFrame([
    (25,35000,5,20,1),
    (30,45000,8,15,0),
    (35,60000,12,30,1),
    (28,40000,6,18,0),
    (45,85000,20,40,1),
    (50,90000,25,35,1),
    (23,30000,2,10,0),
    (32,50000,10,22,1),
    (40,70000,15,28,1),
    (27,38000,4,12,0)
],[
    "age",
    "income",
    "purchase_history",
    "website_visits",
    "label"
])

print("\nDataset")
data.show()

# ---------------------------------------
# Feature Vector
# ---------------------------------------

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

# ---------------------------------------
# Train Model
# ---------------------------------------

rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    numTrees=100,
    seed=42
)

model = rf.fit(dataset)

# ---------------------------------------
# Feature Importance
# ---------------------------------------

feature_names = [
    "Age",
    "Income",
    "Purchase History",
    "Website Visits"
]

importances = model.featureImportances

print("\nFeature Importance\n")

for name, score in zip(feature_names, importances):
    print(f"{name:20} : {score:.4f}")

spark.stop()
