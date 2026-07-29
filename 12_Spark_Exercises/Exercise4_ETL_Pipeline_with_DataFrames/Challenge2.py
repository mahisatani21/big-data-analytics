from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("Data Quality Checks") \
    .getOrCreate()

# Read Data
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
orders = spark.read.csv("orders.csv", header=True, inferSchema=True)
products = spark.read.csv("products.csv", header=True, inferSchema=True)

# -------------------------
# Null Value Check
# -------------------------

print("\nNull Values in Customers")

customers.select([
    count(
        when(col(c).isNull(), c)
    ).alias(c)
    for c in customers.columns
]).show()

print("\nNull Values in Orders")

orders.select([
    count(
        when(col(c).isNull(), c)
    ).alias(c)
    for c in orders.columns
]).show()

print("\nNull Values in Products")

products.select([
    count(
        when(col(c).isNull(), c)
    ).alias(c)
    for c in products.columns
]).show()

# -------------------------
# Duplicate Check
# -------------------------

print("\nDuplicate Customer Records")

print(
    customers.count() -
    customers.dropDuplicates().count()
)

print("\nDuplicate Order Records")

print(
    orders.count() -
    orders.dropDuplicates().count()
)

print("\nDuplicate Product Records")

print(
    products.count() -
    products.dropDuplicates().count()
)

# -------------------------
# Remove Duplicates
# -------------------------

customers_clean = customers.dropDuplicates()
orders_clean = orders.dropDuplicates()
products_clean = products.dropDuplicates()

print("\nCleaned Data Created Successfully")

spark.stop()
