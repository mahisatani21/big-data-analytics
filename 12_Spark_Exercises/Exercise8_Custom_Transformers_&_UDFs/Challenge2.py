from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length

spark = SparkSession.builder \
    .appName("Challenge 2") \
    .getOrCreate()

data = [
    ("Laptop is Awesome"),
    ("PySpark Guide"),
    ("Machine Learning")
]

df = spark.createDataFrame([(x,) for x in data], ["text"])

df = df.withColumn(
    "text_length",
    length(col("text"))
)

print("Custom ML Feature")
df.show()

spark.stop()
