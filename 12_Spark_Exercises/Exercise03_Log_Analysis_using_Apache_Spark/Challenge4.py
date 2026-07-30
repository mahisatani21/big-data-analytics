from pyspark.sql import SparkSession
import re

spark = SparkSession.builder \
    .appName("Failed Login Attempts") \
    .getOrCreate()

sc = spark.sparkContext

log_data = sc.parallelize([
    '192.168.1.2 - - [01/Jan/2024:12:01:00] "POST /login HTTP/1.1" 404',
    '192.168.1.2 - - [01/Jan/2024:12:02:00] "POST /login HTTP/1.1" 404',
    '192.168.1.2 - - [01/Jan/2024:12:03:00] "POST /login HTTP/1.1" 200',
    '192.168.1.3 - - [01/Jan/2024:12:04:00] "POST /login HTTP/1.1" 404',
    '192.168.1.4 - - [01/Jan/2024:12:05:00] "GET /index.html HTTP/1.1" 200'
])

failed = log_data.filter(
    lambda line: "/login" in line and "404" in line
)

ips = failed.map(
    lambda line: re.search(
        r'^(\d+\.\d+\.\d+\.\d+)',
        line
    ).group(1)
)

result = ips.map(
    lambda ip: (ip, 1)
).reduceByKey(
    lambda a, b: a + b
).sortBy(
    lambda x: x[1],
    ascending=False
)

print("Failed Login Attempts")

for row in result.collect():
    print(row)

spark.stop()
