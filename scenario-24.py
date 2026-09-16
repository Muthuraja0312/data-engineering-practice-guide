# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import *
from datetime import date
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, DoubleType

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType, DoubleType
from datetime import date

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PivotExample") \
    .getOrCreate()

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
import datetime

# Initialize Spark
spark = SparkSession.builder.appName("ConsecutiveOrders").getOrCreate()

# Sample data
data = [
    (1, "A", datetime.date(2026, 9, 1)),
    (2, "A", datetime.date(2026, 9, 2)),
    (3, "B", datetime.date(2026, 9, 5)),
    (4, "B", datetime.date(2026, 9, 7)),
    (5, "C", datetime.date(2026, 9, 10)),
    (6, "C", datetime.date(2026, 9, 11)),
]

# Define schema
schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("customer_id", StringType(), True),
    StructField("order_date", DateType(), True)
])

# Create DataFrame
orders_df = spark.createDataFrame(data, schema)

orders_df.show()

orders_df.createOrReplaceTempView("adf")
df1 = spark.sql("select a.customer_id from adf a join adf b on a.customer_id=b.customer_id where date(a.order_date) = date(b.order_date) + interval 1 day")
df1.show()
