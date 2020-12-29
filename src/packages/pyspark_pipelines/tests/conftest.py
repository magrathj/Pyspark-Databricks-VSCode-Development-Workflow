import pytest
import pyspark

@pytest.fixture(scope='session')
def spark():
    spark = pyspark.sql.SparkSession.builder.appName("MyApp") \
            .config("spark.jars.packages", "com.microsoft.ml.spark:mmlspark_2.11:1.0.0-rc1") \
            .config("spark.jars.repositories", "https://mmlspark.azureedge.net/maven") \
            .getOrCreate()
    yield spark
    spark.stop()


@pytest.fixture(scope='session')
def spark_context(spark):
    sc = spark.sparkContext
    yield sc
    spark.stop()


