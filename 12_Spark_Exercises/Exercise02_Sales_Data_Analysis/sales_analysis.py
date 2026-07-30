from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("Sales Data Analysis") \
    .getOrCreate()

# Read CSV File
df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

print("Sales Data")
df.show()

# Revenue Column
df = df.withColumn(
    "revenue",
    col("price") * col("quantity")
)

print("Revenue by Product")
df.groupBy("product").agg(
    sum("revenue").alias("Total Revenue"),
    sum("quantity").alias("Total Quantity")
).show()

print("Revenue by City")
df.groupBy("city").agg(
    sum("revenue").alias("Revenue")
).orderBy(
    col("Revenue").desc()
).show()

spark.stop()
