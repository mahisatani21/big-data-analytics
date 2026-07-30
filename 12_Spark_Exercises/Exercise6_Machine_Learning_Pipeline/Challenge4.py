from flask import Flask, request, jsonify
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier

# ---------------------------------------
# Create Spark Session
# ---------------------------------------

spark = SparkSession.builder \
    .appName("ML REST API") \
    .getOrCreate()

# ---------------------------------------
# Training Data
# ---------------------------------------

data = spark.createDataFrame([
    (25,35000,5,20,1),
    (30,45000,8,15,0),
    (35,60000,12,30,1),
    (40,70000,15,28,1),
    (28,40000,6,18,0),
    (50,90000,25,35,1)
],[
    "age",
    "income",
    "purchase_history",
    "website_visits",
    "label"
])

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

rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    numTrees=50,
    seed=42
)

model = rf.fit(dataset)

# ---------------------------------------
# Flask API
# ---------------------------------------

app = Flask(__name__)

@app.route("/")
def home():
    return "Spark ML REST API Running"

@app.route("/predict", methods=["POST"])
def predict():

    values = request.json

    sample = spark.createDataFrame([
        (
            values["age"],
            values["income"],
            values["purchase_history"],
            values["website_visits"]
        )
    ],[
        "age",
        "income",
        "purchase_history",
        "website_visits"
    ])

    sample = assembler.transform(sample)

    prediction = model.transform(sample)

    result = prediction.select("prediction").collect()[0][0]

    return jsonify({
        "prediction": int(result)
    })

if __name__ == "__main__":
    app.run(debug=True)
