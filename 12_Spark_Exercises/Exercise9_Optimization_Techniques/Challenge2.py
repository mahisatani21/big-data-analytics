from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("Challenge 2") \
    .getOrCreate()

data = [
    ("A",100),
    ("A",150),
    ("A",120),
    ("B",200),
    ("C",300),
    ("D",250)
]

df = spark.createDataFrame(data, ["key","value"])

salted_df = df.withColumn(
    "salted_key",
    concat(
        col("key"),
        lit("_"),
        (rand()*5).cast("int")
    )
)

print("Original Data")
df.show()

print("Salted Data")
salted_df.show()

spark.stop()
