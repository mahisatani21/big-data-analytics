from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# -----------------------------------
# Create Spark Session
# -----------------------------------

spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

# -----------------------------------
# Extract
# -----------------------------------

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

print("\nCustomers Data")
customers.show()

print("\nOrders Data")
orders.show()

print("\nProducts Data")
products.show()

# -----------------------------------
# Transform
# -----------------------------------

customer_orders = customers.join(
    orders,
    "customer_id"
).join(
    products,
    "product_id"
)

print("\nJoined Dataset")
customer_orders.show()

# -----------------------------------
# Customer Lifetime Value
# -----------------------------------

customer_lifetime = customer_orders.groupBy(
    "customer_id",
    "customer_name"
).agg(
    sum("price").alias("Total Spent"),
    count("order_id").alias("Number of Orders"),
    round(avg("price"), 2).alias("Average Order Value")
)

print("\nCustomer Lifetime Value")
customer_lifetime.show()

# -----------------------------------
# Rank Customers
# -----------------------------------

window_spec = Window.orderBy(
    col("Total Spent").desc()
)

ranked_customers = customer_lifetime.withColumn(
    "Rank",
    row_number().over(window_spec)
)

print("\nCustomer Ranking")
ranked_customers.show()

# -----------------------------------
# Running Total
# -----------------------------------

window_running = Window.partitionBy(
    "customer_id"
).orderBy(
    "order_date"
).rowsBetween(
    Window.unboundedPreceding,
    Window.currentRow
)

running_total = customer_orders.withColumn(
    "Running Total",
    sum("price").over(window_running)
)

print("\nRunning Total")
running_total.show()

# -----------------------------------
# Load
# -----------------------------------

ranked_customers.write.mode("overwrite").csv(
    "output/customer_lifetime",
    header=True
)

running_total.write.mode("overwrite").csv(
    "output/running_total",
    header=True
)

print("\nData successfully saved into output folder.")

spark.stop()
