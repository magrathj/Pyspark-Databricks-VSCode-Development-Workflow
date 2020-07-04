import pyspark
spark = pyspark.sql.SparkSession.builder.appName("MyApp") \
            .config("spark.jars.packages", "com.microsoft.ml.spark:mmlspark_2.11:1.0.0-rc1") \
            .config("spark.jars.repositories", "https://mmlspark.azureedge.net/maven") \
            .getOrCreate()


print(f"**************************")
print(f"Spark context set: {spark}")

df = spark.createDataFrame(
    [
        (1, 'foo'), # create your data here, be consistent in the types.
        (2, 'bar'),
    ],
    ['id', 'txt'] # add your columns label here
)

df.show()


print("Pyspark test completed")
print(f"**************************")