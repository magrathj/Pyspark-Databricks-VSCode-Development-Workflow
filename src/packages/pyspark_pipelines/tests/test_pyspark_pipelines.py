import os
import pytest
import numpy as np
import pandas as pd
from numpy.testing import assert_array_equal
from pyspark.sql import SparkSession, DataFrame
from pyspark_pipelines.jobs.data_quality import *


ROOT_DIR = os.getcwd()

@pytest.fixture
def input_df(spark):
    pdf = pd.DataFrame({
        'a': [0,  1, 2],
        'b': [1, -1, 3]
    })    
    df = spark.createDataFrame(pdf)
    return df
    


class TestAddColumnwise:
    def test_returns_dataframe(self, input_df):
        """Return type should be DataFrame."""
        out_df = add_columnwise(input_df, 'a', 'b')
        assert isinstance(out_df, DataFrame)