from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("WordCount_StopWords") \
    .getOrCreate()

# Get Spark Context
sc = spark.sparkContext

# Read file
text_file = sc.textFile("sample.txt")

# Stop Words
stop_words = {"the", "is", "a", "an", "and", "of", "to"}

# Split words and remove stop words
words = text_file.flatMap(lambda line: line.split()) \
                 .filter(lambda word: word.lower() not in stop_words)

# Create (word,1)
word_pairs = words.map(lambda word: (word, 1))

# Count words
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

print("Word Count Without Stop Words:\n")

for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark
spark.stop()
