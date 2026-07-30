from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    udf,
    pandas_udf
)
from pyspark.sql.types import StringType
import pandas as pd
import re

# -----------------------------------
# Create Spark Session
# -----------------------------------
spark = SparkSession.builder \
    .appName("Custom Transformers and UDFs") \
    .getOrCreate()

# -----------------------------------
# Sample Data
# -----------------------------------
data = [
    ("Electronics", "Laptop!!! is Awesome ###"),
    ("Electronics", "Mouse@@ works Great!!!"),
    ("Books", "PySpark -- Guide"),
    ("Books", "Machine Learning@@ Book"),
    ("Clothing", "Men's T-Shirt ###"),
    ("Clothing", "Women's Jacket@@")
]

columns = ["category", "text"]

df = spark.createDataFrame(data, columns)

print("\nOriginal Data")
df.show(truncate=False)

# -----------------------------------
# Regular Python UDF
# -----------------------------------
def clean_text(text):
    if text is None:
        return None
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

clean_udf = udf(clean_text, StringType())

df_clean = df.withColumn(
    "cleaned_text",
    clean_udf(col("text"))
)

print("\nAfter Regular UDF")
df_clean.show(truncate=False)

# -----------------------------------
# Pandas UDF
# -----------------------------------
@pandas_udf(StringType())
def clean_text_pandas(text: pd.Series) -> pd.Series:
    return text.str.replace(
        r'[^a-zA-Z0-9\s]',
        '',
        regex=True
    )

df_pandas = df.withColumn(
    "cleaned_text",
    clean_text_pandas(col("text"))
)

print("\nAfter Pandas UDF")
df_pandas.show(truncate=False)

spark.stop()
