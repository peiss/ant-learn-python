from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("my spark").master("local[2]").getOrCreate()
sc = spark.sparkContext

data = spark.read.text("file:///Users/work/PycharmProjects/test/dict_test/input.txt")

print("data.count:", data.count())
data.wi
spark.stop()
