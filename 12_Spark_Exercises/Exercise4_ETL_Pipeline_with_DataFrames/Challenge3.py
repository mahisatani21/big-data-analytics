from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("Materialized Views") \
    .getOrCreate()

# Read Data
customers = spark.read.csv(
    "customers.csv",
    header=True,
    inferSchema=True
)

orders = spark.read.csv(
    "orders.csv",
    header=True,
    inferSchema=True
)

products = spark.read.csv(
    "products.csv",
    header=True,
    inferSchema=True
)

# Join Data
customer_orders = customers.join(
    orders,
    "customer_id"
).join(
    products,
    "product_id"
)

# Materialized View 1
customer_summary = customer_orders.groupBy(
    "customer_id",
    "customer_name"
).agg(
    count("order_id").alias("Total Orders"),
    sum("price").alias("Total Spent")
)

print("\nCustomer Summary")
customer_summary.show()

# Materialized View 2
product_summary = customer_orders.groupBy(
    "product_name"
).agg(
    count("order_id").alias("Orders"),
    sum("price").alias("Revenue")
)

print("\nProduct Summary")
product_summary.show()

# Save Views
customer_summary.write.mode("overwrite").csv(
    "output/customer_summary",
    header=True
)

product_summary.write.mode("overwrite").csv(
    "output/product_summary",
    header=True
)

print("\nMaterialized Views Created Successfully.")

spark.stop()
