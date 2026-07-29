print("\n Display Top 10 Most Frequent Words")

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Top10Words") \
    .getOrCreate()

# Get Spark Context
sc = spark.sparkContext

# Read file
text_file = sc.textFile("sample.txt")

# Split words
words = text_file.flatMap(lambda line: line.split())

# Create (word,1)
word_pairs = words.map(lambda word: (word, 1))

# Count words
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# Sort by frequency (Highest First)
top_words = word_counts.takeOrdered(
    10,
    key=lambda x: -x[1]
)

print("Top 10 Most Frequent Words:\n")

for word, count in top_words:
    print(f"{word}: {count}")

# Stop Spark
spark.stop()
