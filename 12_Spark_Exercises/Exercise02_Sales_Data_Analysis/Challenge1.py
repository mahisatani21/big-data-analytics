from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("Top 5 Products") \
    .getOrCreate()

df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "revenue",
    col("price") * col("quantity")
)

print("Top 5 Best Selling Products")

df.groupBy("product").agg(
    sum("quantity").alias("Total Quantity")
).orderBy(
    col("Total Quantity").desc()
).show(5)

spark.stop()
