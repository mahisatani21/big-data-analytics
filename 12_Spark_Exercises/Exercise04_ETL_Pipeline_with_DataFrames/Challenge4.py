from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("Slowly Changing Dimensions") \
    .getOrCreate()

# Existing Customer Data
customers = spark.read.csv(
    "customers.csv",
    header=True,
    inferSchema=True
)

print("\nExisting Customer Data")
customers.show()

# Updated Customer Data
updated_data = [
    (101, "Amit", "Delhi"),
    (102, "Priya", "Pune"),
    (103, "Rahul", "Bangalore"),
    (104, "Sneha", "Chennai"),
    (105, "Arjun", "Hyderabad"),
    (106, "Neha", "Mumbai")
]

updated_customers = spark.createDataFrame(
    updated_data,
    ["customer_id", "customer_name", "city"]
)

print("\nUpdated Customer Data")
updated_customers.show()

# Simulate SCD Type-1
final_customers = updated_customers

print("\nFinal Customer Dimension")
final_customers.show()

# Save Updated Dimension
final_customers.write.mode("overwrite").csv(
    "output/customer_dimension",
    header=True
)

print("\nCustomer Dimension Updated Successfully.")

spark.stop()
