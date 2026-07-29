from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("Monthly Revenue Growth") \
    .getOrCreate()

df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "date",
    to_date("date")
)

df = df.withColumn(
    "revenue",
    col("price") * col("quantity")
)

monthly = df.groupBy(
    date_format("date", "yyyy-MM").alias("Month")
).agg(
    sum("revenue").alias("Revenue")
)

window = Window.orderBy("Month")

monthly = monthly.withColumn(
    "Previous Revenue",
    lag("Revenue").over(window)
)

monthly = monthly.withColumn(
    "Growth %",
    round(
        (
            (col("Revenue") - col("Previous Revenue"))
            / col("Previous Revenue")
        ) * 100,
        2
    )
)

print("Month-over-Month Revenue Growth")

monthly.show()

spark.stop()
