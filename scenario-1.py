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

data = [
    ("SEA", "SF", 300),
    ("CHI", "SEA", 2000),
    ("SF", "SEA", 300),
    ("SEA", "CHI", 2000),
    ("SEA", "LND", 500),
    ("LND", "SEA", 500),
    ("LND", "CHI", 1000),
    ("CHI", "NDL", 180)]
df = spark.createDataFrame(data, ["from", "to", "dist"])
df.show()

# Through SQL
df.createOrReplaceTempView("trip")
df2=spark.sql("select a.from,a.to, (a.dist+ b.dist) as total from trip a join trip b on a.from = b.to and a.to = b.from where a.from < a.to")
df2.show()

dfx= df.alias("a").join(df.alias("b"),(col("a.from") == col("b.to")) & (col("a.to") == col("b.from"))).where(col("a.from") < col("a.to")).select(col("a.from"),col("b.to"),(col("a.dist") + col("b.dist")).alias("total"))
dfx.show()
