print("Count Only Words Longer Than 3 Characters")

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("WordCount_LongWords") \
    .getOrCreate()

# Get Spark Context
sc = spark.sparkContext

# Read text file
text_file = sc.textFile("sample.txt")

# Split into words and filter words longer than 3 characters
words = text_file.flatMap(lambda line: line.split()) \
                 .filter(lambda word: len(word) > 3)

# Create (word,1) pairs
word_pairs = words.map(lambda word: (word, 1))

# Count words
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# Print result
print("Words Longer Than 3 Characters:\n")

for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark
spark.stop()
