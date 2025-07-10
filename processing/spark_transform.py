from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HealthcarePipeline") \
    .getOrCreate()

df = spark.read.csv("../data/raw/hospital_data.csv", header=True)

df_clean = df.select(
    "facility_name",
    "state",
    "hospital_type",
    "emergency_services"
)

df_clean.write.mode("overwrite").parquet("../data/processed/hospital_clean")

print("Data transformation complete")