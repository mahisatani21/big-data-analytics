from pyspark.sql import SparkSession
import re

# Create Spark Session
spark = SparkSession.builder \
    .appName("Log Analysis") \
    .getOrCreate()

sc = spark.sparkContext

# Sample Log Data
log_data = sc.parallelize([
    '192.168.1.1 - - [01/Jan/2024:12:00:00] "GET /index.html HTTP/1.1" 200',
    '192.168.1.2 - - [01/Jan/2024:12:01:00] "POST /login HTTP/1.1" 404',
    '192.168.1.3 - - [01/Jan/2024:12:02:00] "GET /about HTTP/1.1" 200',
    '192.168.1.2 - - [01/Jan/2024:12:03:00] "GET /home HTTP/1.1" 500'
])

# Parse Logs
parsed_logs = log_data.map(lambda line: {
    "ip": re.search(r'^(\d+\.\d+\.\d+\.\d+)', line).group(1),
    "timestamp": re.search(r'\[(.*?)\]', line).group(1),
    "method": re.search(r'"(GET|POST|PUT|DELETE)', line).group(1),
    "url": re.search(r'"(?:GET|POST|PUT|DELETE)\s(.*?)\sHTTP', line).group(1),
    "status": re.search(r'(\d{3})$', line).group(1)
})

print("Parsed Logs")
for log in parsed_logs.collect():
    print(log)

print("\nStatus Code Count")
status_counts = parsed_logs.map(
    lambda x: (x["status"], 1)
).reduceByKey(
    lambda a, b: a + b
)

for status, count in status_counts.collect():
    print(status, count)

print("\nIP Address Count")
ip_counts = parsed_logs.map(
    lambda x: (x["ip"], 1)
).reduceByKey(
    lambda a, b: a + b
)

for ip, count in ip_counts.collect():
    print(ip, count)

spark.stop()
