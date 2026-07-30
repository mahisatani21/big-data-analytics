from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("Average Order Value") \
    .getOrCreate()

df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "OrderValue",
    col("price") * col("quantity")
)

print("Products with Highest Average Order Value")

df.groupBy("product").agg(
    round(
        avg("OrderValue"),
        2
    ).alias("Average Order Value")
).orderBy(
    col("Average Order Value").desc()
).show()

spark.stop()
