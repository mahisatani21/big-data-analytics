"""
E-Commerce Sales Analysis using Hadoop + Spark
UCI Online Retail Dataset

Run with:
    spark-submit --master local[*] --driver-memory 2g ecommerce_analysis.py

Prerequisites:
    - Hadoop HDFS running (start-dfs.sh)
    - Dataset uploaded to HDFS at HDFS_INPUT_PATH (see PROJECT_GUIDE.md section 4)
"""

import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, DoubleType, TimestampType
)

# ---------------------------------------------------------------------------
# 0. CONFIG — edit these two paths for your environment
# ---------------------------------------------------------------------------
HDFS_USER = "mahi"
HDFS_INPUT_PATH = f"/user/{HDFS_USER}/ecommerce/input/online_retail.csv"
HDFS_OUTPUT_PATH = f"/user/{HDFS_USER}/ecommerce/output"
LOCAL_CHART_DIR = os.path.expanduser("~/ecommerce-bigdata/charts")

os.makedirs(LOCAL_CHART_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. SPARK SESSION
# ---------------------------------------------------------------------------
spark = (
    SparkSession.builder
    .appName("EcommerceSalesAnalysis")
    .config("spark.sql.shuffle.partitions", "8")   # small cluster -> fewer shuffle partitions
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

print("=" * 70)
print("STEP 1: Reading raw data from HDFS")
print("=" * 70)

schema = StructType([
    StructField("InvoiceNo", StringType(), True),
    StructField("StockCode", StringType(), True),
    StructField("Description", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("InvoiceDate", StringType(), True),   # parsed to timestamp below
    StructField("UnitPrice", DoubleType(), True),
    StructField("CustomerID", StringType(), True),
    StructField("Country", StringType(), True),
])

raw_df = (
    spark.read
    .option("header", "true")
    .option("mode", "PERMISSIVE")
    .schema(schema)
    .csv(HDFS_INPUT_PATH)
)

raw_count = raw_df.count()
print(f"Raw row count: {raw_count:,}")

# ---------------------------------------------------------------------------
# 2. DATA CLEANING
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("STEP 2: Cleaning data")
print("=" * 70)

df = raw_df.withColumn(
    "InvoiceDate",
    F.to_timestamp("InvoiceDate", "yyyy-MM-dd HH:mm:ss")
)

# Remove cancellations (InvoiceNo starting with 'C'), null customers,
# non-positive quantity/price, and blank descriptions.
clean_df = (
    df.filter(~F.col("InvoiceNo").startswith("C"))
      .filter(F.col("CustomerID").isNotNull())
      .filter(F.col("Quantity") > 0)
      .filter(F.col("UnitPrice") > 0)
      .filter(F.col("Description").isNotNull())
      .withColumn("CustomerID", F.col("CustomerID").cast(IntegerType()))
      .withColumn("TotalPrice", F.round(F.col("Quantity") * F.col("UnitPrice"), 2))
      .dropDuplicates()
)

clean_count = clean_df.count()
print(f"Clean row count: {clean_count:,}")
print(f"Rows removed: {raw_count - clean_count:,} "
      f"({(raw_count - clean_count) / raw_count:.1%})")

clean_df.cache()
clean_df.createOrReplaceTempView("sales")

# Persist cleaned data back to HDFS for reuse (e.g. Hive external table)
clean_df.write.mode("overwrite").parquet(f"{HDFS_OUTPUT_PATH}/cleaned_data_parquet")

# ---------------------------------------------------------------------------
# 3. ANALYSIS 1 — Revenue by Country
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ANALYSIS 1: Revenue by Country")
print("=" * 70)

revenue_by_country = spark.sql("""
    SELECT Country, ROUND(SUM(TotalPrice), 2) AS Revenue, COUNT(DISTINCT InvoiceNo) AS Orders
    FROM sales
    GROUP BY Country
    ORDER BY Revenue DESC
""")
revenue_by_country.show(10, truncate=False)
revenue_by_country.write.mode("overwrite").option("header", "true") \
    .csv(f"{HDFS_OUTPUT_PATH}/revenue_by_country_csv")
revenue_by_country.write.mode("overwrite").parquet(f"{HDFS_OUTPUT_PATH}/revenue_by_country_parquet")

# ---------------------------------------------------------------------------
# 4. ANALYSIS 2 — Monthly Sales Trend
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ANALYSIS 2: Monthly Sales Trend")
print("=" * 70)

monthly_trend = spark.sql("""
    SELECT DATE_FORMAT(InvoiceDate, 'yyyy-MM') AS Month,
           ROUND(SUM(TotalPrice), 2) AS Revenue,
           COUNT(DISTINCT InvoiceNo) AS Orders
    FROM sales
    GROUP BY DATE_FORMAT(InvoiceDate, 'yyyy-MM')
    ORDER BY Month
""")
monthly_trend.show(20, truncate=False)
monthly_trend.write.mode("overwrite").option("header", "true") \
    .csv(f"{HDFS_OUTPUT_PATH}/monthly_trend_csv")

# ---------------------------------------------------------------------------
# 5. ANALYSIS 3 — Top 10 Best-Selling Products
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ANALYSIS 3: Top 10 Best-Selling Products (by quantity)")
print("=" * 70)

top_products = spark.sql("""
    SELECT Description,
           SUM(Quantity) AS TotalQuantity,
           ROUND(SUM(TotalPrice), 2) AS Revenue
    FROM sales
    GROUP BY Description
    ORDER BY TotalQuantity DESC
    LIMIT 10
""")
top_products.show(10, truncate=False)
top_products.write.mode("overwrite").option("header", "true") \
    .csv(f"{HDFS_OUTPUT_PATH}/top_products_csv")

# ---------------------------------------------------------------------------
# 6. ANALYSIS 4 — Cancellation Rate (computed from raw, pre-clean data)
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ANALYSIS 4: Order Cancellation Rate")
print("=" * 70)

total_invoices = df.select("InvoiceNo").distinct().count()
cancelled_invoices = df.filter(F.col("InvoiceNo").startswith("C")) \
                        .select("InvoiceNo").distinct().count()
cancel_rate = cancelled_invoices / total_invoices
print(f"Total distinct invoices : {total_invoices:,}")
print(f"Cancelled invoices      : {cancelled_invoices:,}")
print(f"Cancellation rate       : {cancel_rate:.2%}")

# ---------------------------------------------------------------------------
# 7. ANALYSIS 5 — RFM Customer Segmentation
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ANALYSIS 5: RFM Customer Segmentation")
print("=" * 70)

max_date = clean_df.agg(F.max("InvoiceDate")).collect()[0][0]
snapshot_date = F.lit(max_date) + F.expr("INTERVAL 1 DAY")

rfm = clean_df.groupBy("CustomerID").agg(
    F.datediff(snapshot_date, F.max("InvoiceDate")).alias("Recency"),
    F.countDistinct("InvoiceNo").alias("Frequency"),
    F.round(F.sum("TotalPrice"), 2).alias("Monetary"),
)

# Score each dimension into quintiles (1-5) using Spark's window + ntile
# Higher score = better customer
def add_score(dataframe, col, ascending, out_col):
    order_col = F.col(col).asc() if ascending else F.col(col).desc()
    w = Window.orderBy(order_col)
    return dataframe.withColumn(out_col, 6 - F.ntile(5).over(w))

rfm = add_score(rfm, "Recency", ascending=True, out_col="R_Score")
rfm = add_score(rfm, "Frequency", ascending=False, out_col="F_Score")
rfm = add_score(rfm, "Monetary", ascending=False, out_col="M_Score")

rfm = rfm.withColumn(
    "RFM_Segment",
    F.concat_ws("", F.col("R_Score"), F.col("F_Score"), F.col("M_Score"))
)

rfm = rfm.withColumn(
    "CustomerTier",
    F.when((F.col("R_Score") >= 4) & (F.col("F_Score") >= 4) & (F.col("M_Score") >= 4), "Champion")
     .when((F.col("R_Score") >= 3) & (F.col("F_Score") >= 3), "Loyal")
     .when((F.col("R_Score") <= 2) & (F.col("F_Score") <= 2), "At Risk / Lost")
     .otherwise("Regular")
)

rfm.orderBy(F.col("Monetary").desc()).show(10, truncate=False)

tier_counts = rfm.groupBy("CustomerTier").count().orderBy(F.col("count").desc())
tier_counts.show(truncate=False)

rfm.write.mode("overwrite").option("header", "true").csv(f"{HDFS_OUTPUT_PATH}/rfm_csv")
rfm.write.mode("overwrite").parquet(f"{HDFS_OUTPUT_PATH}/rfm_parquet")

# ---------------------------------------------------------------------------
# 8. ANALYSIS 6 — Top Customers by Lifetime Spend
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ANALYSIS 6: Top 10 Customers by Lifetime Spend")
print("=" * 70)

top_customers = rfm.orderBy(F.col("Monetary").desc()).limit(10)
top_customers.show(10, truncate=False)
top_customers.write.mode("overwrite").option("header", "true") \
    .csv(f"{HDFS_OUTPUT_PATH}/top_customers_csv")

# ---------------------------------------------------------------------------
# 9. VISUALIZATION (small aggregates -> Pandas -> Matplotlib)
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("STEP 9: Generating charts")
print("=" * 70)

import matplotlib
matplotlib.use("Agg")  # headless backend, no display needed in WSL
import matplotlib.pyplot as plt

# Chart 1: Revenue by country
pdf1 = revenue_by_country.limit(10).toPandas()
plt.figure(figsize=(10, 6))
plt.barh(pdf1["Country"][::-1], pdf1["Revenue"][::-1], color="#1D9E75")
plt.xlabel("Revenue (£)")
plt.title("Top 10 Countries by Revenue")
plt.tight_layout()
plt.savefig(f"{LOCAL_CHART_DIR}/revenue_by_country.png", dpi=150)
plt.close()

# Chart 2: Monthly sales trend
pdf2 = monthly_trend.toPandas()
plt.figure(figsize=(10, 6))
plt.plot(pdf2["Month"], pdf2["Revenue"], marker="o", color="#378ADD")
plt.xticks(rotation=45)
plt.ylabel("Revenue (£)")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig(f"{LOCAL_CHART_DIR}/monthly_sales_trend.png", dpi=150)
plt.close()

# Chart 3: Top products
pdf3 = top_products.toPandas()
plt.figure(figsize=(10, 6))
plt.barh(pdf3["Description"][::-1], pdf3["TotalQuantity"][::-1], color="#D85A30")
plt.xlabel("Total Quantity Sold")
plt.title("Top 10 Best-Selling Products")
plt.tight_layout()
plt.savefig(f"{LOCAL_CHART_DIR}/top_products.png", dpi=150)
plt.close()

# Chart 4: RFM segment distribution
pdf4 = tier_counts.toPandas()
plt.figure(figsize=(8, 6))
plt.bar(pdf4["CustomerTier"], pdf4["count"], color="#7F77DD")
plt.ylabel("Number of Customers")
plt.title("Customer Distribution by RFM Tier")
plt.tight_layout()
plt.savefig(f"{LOCAL_CHART_DIR}/rfm_segments.png", dpi=150)
plt.close()

print(f"Charts saved to: {LOCAL_CHART_DIR}")

# ---------------------------------------------------------------------------
# 10. DONE
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("PIPELINE COMPLETE")
print(f"Results in HDFS under: {HDFS_OUTPUT_PATH}")
print(f"Charts saved locally under: {LOCAL_CHART_DIR}")
print("=" * 70)

spark.stop()
