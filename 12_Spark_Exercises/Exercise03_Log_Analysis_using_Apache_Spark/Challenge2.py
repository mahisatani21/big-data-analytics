from pyspark.sql import SparkSession
import re

spark = SparkSession.builder \
    .appName("Error Rate") \
    .getOrCreate()

sc = spark.sparkContext

log_data = sc.parallelize([
    '192.168.1.1 - - [01/Jan/2024:12:00:00] "GET /index.html HTTP/1.1" 200',
    '192.168.1.2 - - [01/Jan/2024:12:01:00] "POST /login HTTP/1.1" 404',
    '192.168.1.3 - - [01/Jan/2024:12:02:00] "GET /about HTTP/1.1" 500',
    '192.168.1.4 - - [01/Jan/2024:12:03:00] "GET /home HTTP/1.1" 200'
])

statuses = log_data.map(
    lambda line: re.search(
        r'(\d{3})$',
        line
    ).group(1)
)

total = statuses.count()

errors = statuses.filter(
    lambda x: x.startswith("4") or x.startswith("5")
).count()

error_rate = (errors / total) * 100

print("Total Requests :", total)
print("Error Requests :", errors)
print("Error Rate :", round(error_rate, 2), "%")

spark.stop()
