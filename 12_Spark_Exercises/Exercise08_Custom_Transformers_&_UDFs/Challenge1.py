from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, split, size

spark = SparkSession.builder \
    .appName("Challenge 1") \
    .getOrCreate()

data = [
    ("Electronics", "Laptop is AWESOME!!!"),
    ("Books", "PySpark Programming Guide"),
    ("Clothing", "Men T-Shirt ###")
]

df = spark.createDataFrame(data, ["category", "text"])

df = df.withColumn(
    "clean_text",
    regexp_replace(lower(col("text")), "[^a-zA-Z0-9 ]", "")
)

df = df.withColumn(
    "word_count",
    size(split(col("clean_text"), " "))
)

print("Custom Feature Extraction")
df.show(truncate=False)

spark.stop()
