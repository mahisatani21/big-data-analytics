from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


# Create Spark Session
spark = SparkSession.builder \
    .appName("StreamingAnalytics") \
    .master("local[*]") \
    .config(
        "spark.sql.streaming.checkpointLocation",
        "./checkpoint"
    ) \
    .getOrCreate()


spark.sparkContext.setLogLevel("WARN")


# Define schema for incoming Kafka messages
schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("event_type", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("value", DoubleType(), True)
])


# Read streaming data from Kafka
input_stream = spark.readStream \
    .format("kafka") \
    .option(
        "kafka.bootstrap.servers",
        "localhost:9092"
    ) \
    .option(
        "subscribe",
        "user_events"
    ) \
    .option(
        "startingOffsets",
        "latest"
    ) \
    .load()


# Convert Kafka value from binary to JSON
events = input_stream \
    .select(
        from_json(
            col("value").cast("string"),
            schema
        ).alias("data")
    ) \
    .select("data.*")


# Apply watermark and window aggregation
windowed_counts = events \
    .withWatermark(
        "timestamp",
        "10 minutes"
    ) \
    .groupBy(
        window(
            col("timestamp"),
            "5 minutes",
            "1 minute"
        ),
        col("event_type")
    ) \
    .agg(
        count("*").alias("event_count"),
        sum("value").alias("total_value"),
        avg("value").alias("average_value")
    )


# Display streaming output
query = windowed_counts.writeStream \
    .outputMode("append") \
    .format("console") \
    .option(
        "truncate",
        "false"
    ) \
    .start()


query.awaitTermination()
