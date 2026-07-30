from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover
from pyspark.ml import Pipeline

spark = SparkSession.builder \
    .appName("Challenge 3") \
    .getOrCreate()

data = [
    ("Laptop is awesome"),
    ("PySpark is powerful"),
    ("Machine learning with Spark")
]

df = spark.createDataFrame([(x,) for x in data], ["text"])

tokenizer = Tokenizer(
    inputCol="text",
    outputCol="words"
)

remover = StopWordsRemover(
    inputCol="words",
    outputCol="filtered_words"
)

pipeline = Pipeline(
    stages=[tokenizer, remover]
)

model = pipeline.fit(df)

result = model.transform(df)

print("Text Preprocessing Pipeline")
result.show(truncate=False)

spark.stop()
