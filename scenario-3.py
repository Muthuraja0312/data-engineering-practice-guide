# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("VisitsTransactions").getOrCreate()
# Sample data
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("TeamsDF").getOrCreate()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CustomerOrders").getOrCreate()


data = [(1, "26-May", 100),
        (1, "27-May", 200),
        (1, "28-May", 300),
        (2, "29-May", 400),
        (3, "30-May", 500),
        (3, "31-May", 600)]
df = spark.createDataFrame(data, ["pid", "date", "price"])
df.show()
df.createOrReplaceTempView("adf")
dfa = spark.sql("select*, sum(price) over(partition by pid order by date) as new_price from adf ")

dfa.show()

winspec = Window.partitionBy("pid").orderBy("date")
df1 = df.withColumn("new_price",(sum(col("price"))).over(winspec))
df1.show()
