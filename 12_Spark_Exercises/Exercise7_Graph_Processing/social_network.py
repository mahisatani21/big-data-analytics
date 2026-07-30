from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# ---------------------------------------
# Create Spark Session
# ---------------------------------------

spark = SparkSession.builder \
    .appName("Graph Processing using DataFrames") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ---------------------------------------
# Create Vertices (Users)
# ---------------------------------------

users = [
    ("1", "John", 30),
    ("2", "Jane", 25),
    ("3", "Bob", 35),
    ("4", "Alice", 28),
    ("5", "David", 40)
]

vertices = spark.createDataFrame(
    users,
    ["user_id", "name", "age"]
)

# ---------------------------------------
# Create Edges (Relationships)
# ---------------------------------------

relationships = [
    ("1", "2", "follows"),
    ("2", "3", "follows"),
    ("1", "3", "friend"),
    ("3", "4", "friend"),
    ("4", "5", "follows"),
    ("5", "1", "friend"),
    ("2", "5", "friend"),
    ("3", "1", "follows")
]

edges = spark.createDataFrame(
    relationships,
    ["src", "dst", "relationship"]
)

# ---------------------------------------
# Display Vertices
# ---------------------------------------

print("\n========== USERS ==========")
vertices.show()

# ---------------------------------------
# Display Edges
# ---------------------------------------

print("\n========== RELATIONSHIPS ==========")
edges.show()

# ---------------------------------------
# Out Degree
# ---------------------------------------

print("\n========== OUT DEGREE ==========")

out_degree = edges.groupBy("src") \
    .agg(count("*").alias("out_degree")) \
    .orderBy(col("out_degree").desc())

out_degree.show()

# ---------------------------------------
# In Degree
# ---------------------------------------

print("\n========== IN DEGREE ==========")

in_degree = edges.groupBy("dst") \
    .agg(count("*").alias("in_degree")) \
    .orderBy(col("in_degree").desc())

in_degree.show()

# ---------------------------------------
# Total Degree
# ---------------------------------------

print("\n========== TOTAL DEGREE ==========")

total_degree = out_degree.join(
    in_degree,
    out_degree.src == in_degree.dst,
    "outer"
).select(
    col("src").alias("user"),
    col("out_degree"),
    col("in_degree")
).fillna(0)

total_degree = total_degree.withColumn(
    "total_degree",
    col("out_degree") + col("in_degree")
)

total_degree.orderBy(
    col("total_degree").desc()
).show()

# ---------------------------------------
# Most Connected Users
# ---------------------------------------

print("\n========== MOST CONNECTED USERS ==========")

most_connected = total_degree.join(
    vertices,
    total_degree.user == vertices.user_id
).select(
    "name",
    "total_degree"
).orderBy(
    col("total_degree").desc()
)

most_connected.show()

# ---------------------------------------
# Friend Relationships
# ---------------------------------------

print("\n========== FRIEND RELATIONSHIPS ==========")

friends = edges.filter(
    col("relationship") == "friend"
)

friends.show()

# ---------------------------------------
# Follower Relationships
# ---------------------------------------

print("\n========== FOLLOWER RELATIONSHIPS ==========")

followers = edges.filter(
    col("relationship") == "follows"
)

followers.show()

# ---------------------------------------
# Number of Friends
# ---------------------------------------

print("\n========== FRIEND COUNT ==========")

friend_count = friends.groupBy("src") \
    .agg(count("*").alias("friends"))

friend_count.show()

# ---------------------------------------
# Number of Followers
# ---------------------------------------

print("\n========== FOLLOWER COUNT ==========")

follower_count = followers.groupBy("dst") \
    .agg(count("*").alias("followers"))

follower_count.show()

spark.stop()
