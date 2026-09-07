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

data = [(1,60000,2018),(1,70000,2019),(1,80000,2020),(2,60000,2018),(2,65000,2019),(2,65000,2020),(3,60000,2018),(3,65000,2019)]

df = spark.createDataFrame(data,["empid","salary","year"])

df.show()

df.createOrReplaceTempView("adf")
df1 = spark.sql("select empid,year,salary,coalesce(salary - lag(salary) over(partition by empid order by year),0) as newsal from adf")
df1.show()

winspec = Window.partitionBy("empid").orderBy("year")
dfx = df.withColumn("newsal", lag("salary").over(winspec))
dfy= dfx.withColumn("newsal",expr("salary - newsal"))
dfz=dfy.withColumn("newsal",coalesce(col("newsal"),lit(0)))
dfz.show()
