from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# -------------------------------------
# Create Spark Session
# -------------------------------------
spark = SparkSession.builder \
    .appName("Complex Event Processing") \
    .getOrCreate()

# -------------------------------------
# Event Schema
# -------------------------------------
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("event_type", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("amount", DoubleType(), True)
])

# -------------------------------------
# Sample Events
# -------------------------------------
data = [
    ("U1", "login",    "2024-01-01 10:00:00", 0.0),
    ("U1", "purchase", "2024-01-01 10:04:00", 1200.0),
    ("U2", "login",    "2024-01-01 11:00:00", 0.0),
    ("U2", "purchase", "2024-01-01 11:20:00", 250.0),
    ("U3", "purchase", "2024-01-01 12:00:00", 1800.0),
    ("U3", "purchase", "2024-01-01 12:05:00", 1700.0)
]

events = spark.createDataFrame(data, [
    "user_id",
    "event_type",
    "timestamp",
    "amount"
]).withColumn(
    "timestamp",
    to_timestamp("timestamp")
)

print("\nOriginal Events")
events.show(truncate=False)

# -------------------------------------
# Pattern Detection
# Login -> Purchase
# -------------------------------------
login = events.filter(col("event_type") == "login")

purchase = events.filter(col("event_type") == "purchase")

pattern = login.alias("l").join(
    purchase.alias("p"),
    col("l.user_id") == col("p.user_id")
).filter(
    (unix_timestamp(col("p.timestamp"))
     - unix_timestamp(col("l.timestamp"))) <= 300
)

print("\nLogin -> Purchase within 5 Minutes")
pattern.select(
    col("l.user_id"),
    col("l.timestamp").alias("login_time"),
    col("p.timestamp").alias("purchase_time"),
    col("p.amount")
).show(truncate=False)

# -------------------------------------
# Session Aggregation
# -------------------------------------
session = events.groupBy("user_id").agg(
    count("*").alias("events_in_session"),
    sum("amount").alias("total_amount")
)

print("\nSession Aggregation")
session.show()

# -------------------------------------
# Fraud Rule Engine
# -------------------------------------
transactions = events.filter(
    col("event_type") == "purchase"
)

fraud = transactions.groupBy("user_id").agg(
    count("*").alias("transaction_count"),
    sum("amount").alias("total_amount"),
    avg("amount").alias("avg_amount")
).filter(
    (col("transaction_count") > 1) |
    (col("avg_amount") > 1000)
)

print("\nFraud Detection")
fraud.show()

spark.stop()
