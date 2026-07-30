from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder \
    .appName("Challenge 3") \
    .getOrCreate()

orders = [
    (1,"Laptop"),
    (2,"Mouse"),
    (3,"Keyboard")
]

products = [
    (1,"Electronics"),
    (2,"Accessories"),
    (3,"Accessories")
]

orders_df = spark.createDataFrame(
    orders,
    ["id","product"]
)

products_df = spark.createDataFrame(
    products,
    ["id","category"]
)

result = orders_df.join(
    broadcast(products_df),
    "id"
)

result.show()

spark.stop()
