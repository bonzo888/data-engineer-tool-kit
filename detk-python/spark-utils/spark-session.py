from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .master("local") \
    .appName("test") \
    .enableHiveSupport() \
    .getOrCreate()