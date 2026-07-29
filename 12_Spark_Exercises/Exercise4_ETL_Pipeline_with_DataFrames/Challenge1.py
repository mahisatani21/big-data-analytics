from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("Sales Dashboard Pipeline") \
    .getOrCreate()

# Read Data
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
products = spark.read.csv("products.csv", header=True, inferSchema=True)

# Join Data
sales = customers.join(orders, "customer_id") \
                 .join(products, "product_id")

# Revenue Column
sales = sales.withColumn(
    "revenue",
    col("price")
)

print("\nTotal Revenue")
sales.select(sum("revenue").alias("Total Revenue")).show()

print("\nRevenue by Product")
sales.groupBy("product_name").agg(
    sum("revenue").alias("Revenue")
).orderBy(
    col("Revenue").desc()
).show()

print("\nRevenue by Customer")
sales.groupBy("customer_name").agg(
    sum("revenue").alias("Revenue")
).orderBy(
    col("Revenue").desc()
).show()

print("\nRevenue by City")
sales.groupBy("city").agg(
    sum("revenue").alias("Revenue")
).orderBy(
    col("Revenue").desc()
).show()

spark.stop()
