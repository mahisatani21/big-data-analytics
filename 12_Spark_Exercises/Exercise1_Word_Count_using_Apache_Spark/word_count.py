from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Get Spark Context
sc = spark.sparkContext

# Read text file
text_file = sc.textFile("sample.txt")

# Split each line into words
words = text_file.flatMap(lambda line: line.split())

# Convert each word into (word, 1)
word_pairs = words.map(lambda word: (word, 1))

# Count occurrences
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# Collect and print
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark
spark.stop()
