from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark import StorageLevel

# ---------------------------------
# Create Spark Session
# ---------------------------------
spark = SparkSession.builder \
    .appName("Spark Optimization Techniques") \
    .getOrCreate()

# ---------------------------------
# Create Sample Data
# ---------------------------------
data = [
    (1, "Laptop", 1000),
    (2, "Mouse", 50),
    (3, "Keyboard", 80),
    (4, "Monitor", 300),
    (5, "Printer", 250)
]

columns = ["id", "product", "price"]

df = spark.createDataFrame(data, columns)

print("\nOriginal Data")
df.show()

# ---------------------------------
# 1. Partition Tuning
# ---------------------------------
print("\nCurrent Partitions:")
print(df.rdd.getNumPartitions())

df_repartition = df.repartition(4)

print("Partitions After Repartition:")
print(df_repartition.rdd.getNumPartitions())

df_coalesce = df_repartition.coalesce(2)

print("Partitions After Coalesce:")
print(df_coalesce.rdd.getNumPartitions())

# ---------------------------------
# 2. Broadcast Join
# ---------------------------------
small_data = [
    (1, "Electronics"),
    (2, "Accessories"),
    (3, "Accessories"),
    (4, "Electronics"),
    (5, "Office")
]

small_df = spark.createDataFrame(
    small_data,
    ["id", "category"]
)

joined_df = df.join(
    broadcast(small_df),
    "id"
)

print("\nBroadcast Join")
joined_df.show()

# ---------------------------------
# 3. Cache DataFrame
# ---------------------------------
df.cache()

print("\nCached Data")
df.show()

# ---------------------------------
# Persist
# ---------------------------------
df.persist(StorageLevel.MEMORY_AND_DISK)

# ---------------------------------
# 4. Adaptive Query Execution
# ---------------------------------
spark.conf.set(
    "spark.sql.adaptive.enabled",
    "true"
)

spark.conf.set(
    "spark.sql.adaptive.coalescePartitions.enabled",
    "true"
)

spark.conf.set(
    "spark.sql.shuffle.partitions",
    "4"
)

print("\nAdaptive Query Execution Enabled")

# ---------------------------------
# 5. Data Skew Handling
# ---------------------------------
df_salted = df.withColumn(
    "salted_key",
    concat(
        col("id"),
        lit("_"),
        (rand()*10).cast("int")
    )
)

print("\nSalted Keys")
df_salted.show()

spark.stop()
