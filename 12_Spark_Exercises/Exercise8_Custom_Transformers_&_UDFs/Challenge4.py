from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, col
from pyspark.sql.types import IntegerType
import pandas as pd

spark = SparkSession.builder \
    .appName("Challenge 4") \
    .getOrCreate()

data = [
    ("Laptop"),
    ("Mouse"),
    ("Keyboard"),
    ("Monitor")
]

df = spark.createDataFrame([(x,) for x in data], ["text"])

@pandas_udf(IntegerType())
def text_length(text: pd.Series) -> pd.Series:
    return text.str.len()

result = df.withColumn(
    "length",
    text_length(col("text"))
)

print("Pandas UDF Performance")
result.show()

spark.stop()
