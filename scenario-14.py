# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NullHandlingPractice").getOrCreate()

data = [
    (1, "Alice", "North", 10, 200),
    (2, "Bob", None, None, 150),
    (3, None, "East", 5, None),
    (4, "David", None, None, None),
    (5, "Eve", "West", 8, 300),
    (5, "Eve", "West", 8, 300),   # duplicate row
    (6, None, None, None, None)   # all nulls
]

columns = ["id", "Name", "Region", "unitsold", "revenue"]

df = spark.createDataFrame(data, columns)
df.show()

df1 = df.na.drop("all",subset=["name"])
df1.show()

df2 = df.na.fill({"Name": "unknown"})
df2.show()

df3 = df.dropDuplicates()
df3.show()
