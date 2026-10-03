from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_date,
    sum,
    avg,
    count,
    when
)

spark = SparkSession.builder.appName(
    "SalesPipelineTransformation"
).getOrCreate()

# Read raw data
df = spark.read.option("header", True).csv(
    "/mnt/data/raw/sales_data.csv"
)

# Convert data types
df = (
    df
    .withColumn("quantity", col("quantity").cast("integer"))
    .withColumn("amount", col("amount").cast("double"))
    .withColumn(
        "transaction_date",
        to_date(col("transaction_date"), "yyyy-MM-dd")
    )
)

# Data validation
invalid_records = df.filter(
    col("customer_id").isNull()
    | col("transaction_date").isNull()
    | (col("amount") < 0)
)

print("Invalid records:", invalid_records.count())

# Remove invalid records
clean_df = df.filter(
    col("customer_id").isNotNull()
    & col("transaction_date").isNotNull()
    & (col("amount") >= 0)
)

# Remove duplicates
clean_df = clean_df.dropDuplicates(
    ["transaction_id"]
)

# Revenue by country
country_summary = (
    clean_df
    .groupBy("country")
    .agg(
        count("*").alias("transaction_count"),
        sum("amount").alias("total_revenue"),
        avg("amount").alias("average_transaction")
    )
)

country_summary.show()

# Save processed data
clean_df.write.mode("overwrite").parquet(
    "/mnt/data/processed/sales"
)

country_summary.write.mode("overwrite").parquet(
    "/mnt/data/processed/country_summary"
)

spark.stop()
