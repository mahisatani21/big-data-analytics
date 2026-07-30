from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# -------------------------------------
# Create Spark Session
# -------------------------------------
spark = SparkSession.builder \
    .appName("E-Commerce Analytics Platform") \
    .getOrCreate()

# -------------------------------------
# Sample Orders Data
# -------------------------------------
orders_data = [
    (1, "2024-01-01", 101, 1001, 2, 2000.0),
    (2, "2024-01-01", 102, 1002, 1, 800.0),
    (3, "2024-01-02", 101, 1003, 3, 1500.0),
    (4, "2024-01-02", 103, 1001, 1, 1000.0),
    (5, "2024-01-03", 102, 1002, 2, 1600.0)
]

orders = spark.createDataFrame(
    orders_data,
    [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "total_amount"
    ]
)

# -------------------------------------
# Sample Customers Data
# -------------------------------------
customers_data = [
    (101, "John"),
    (102, "Alice"),
    (103, "Bob")
]

customers = spark.createDataFrame(
    customers_data,
    ["customer_id", "customer_name"]
)

# -------------------------------------
# Sample Products Data
# -------------------------------------
products_data = [
    (1001, "Laptop"),
    (1002, "Mobile"),
    (1003, "Headphones")
]

products = spark.createDataFrame(
    products_data,
    ["product_id", "product_name"]
)

# -------------------------------------
# Analytics Class
# -------------------------------------
class ECommerceAnalytics:

    def __init__(self, spark):
        self.spark = spark

    def compute_metrics(self, orders):

        # Daily Sales
        daily_sales = orders.groupBy("order_date").agg(
            sum("total_amount").alias("daily_revenue"),
            count("order_id").alias("order_count")
        )

        # Customer Metrics
        customer_metrics = orders.groupBy("customer_id").agg(
            sum("total_amount").alias("lifetime_value"),
            count("order_id").alias("order_count"),
            avg("total_amount").alias("avg_order_value")
        )

        # Product Metrics
        product_metrics = orders.groupBy("product_id").agg(
            sum("quantity").alias("total_units_sold"),
            sum("total_amount").alias("product_revenue")
        )

        return (
            daily_sales,
            customer_metrics,
            product_metrics
        )


analytics = ECommerceAnalytics(spark)

daily_sales, customer_metrics, product_metrics = \
analytics.compute_metrics(orders)

print("\nDaily Sales")
daily_sales.show()

print("\nCustomer Metrics")
customer_metrics.show()

print("\nProduct Metrics")
product_metrics.show()

spark.stop()
