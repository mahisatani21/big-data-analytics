from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Challenge 1") \
    .getOrCreate()

data = [(i, f"Product{i}", i * 100) for i in range(1, 101)]

df = spark.createDataFrame(data, ["id", "product", "price"])

print("Execution Plan Before Optimization")
df.explain()

optimized_df = df.repartition(4)

print("\nExecution Plan After Optimization")
optimized_df.explain()

optimized_df.show(10)

spark.stop()
