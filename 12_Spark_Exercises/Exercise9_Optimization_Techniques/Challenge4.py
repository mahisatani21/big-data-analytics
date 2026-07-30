from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Challenge 4") \
    .getOrCreate()

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

print("Spark Optimization Settings")

print("Adaptive Enabled:",
      spark.conf.get("spark.sql.adaptive.enabled"))

print("Coalesce Partitions:",
      spark.conf.get("spark.sql.adaptive.coalescePartitions.enabled"))

print("Shuffle Partitions:",
      spark.conf.get("spark.sql.shuffle.partitions"))

spark.stop()
