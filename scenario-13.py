# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession
data = [(1, 101, '2024-01-01', 100.00),
(2, 101, '2024-01-03', 200.00),
(3, 101, '2024-01-05', 300.00),
(4, 102, '2024-01-02', 150.00),
(5, 102, '2024-01-06', 250.00),
(6, 103, '2024-01-04', 500.00),
(7, 103, '2024-01-08', 100.00)]

df = spark.createDataFrame(data,["transaction_id","customer_id","transaction_date","amount"])
df.show()

df.createOrReplaceTempView("adf")
df1 = spark.sql("select *,sum(amount) over (partition by customer_id order by transaction_date ) as rolling from adf ")
df1.show()

win = Window.partitionBy("customer_id").orderBy("transaction_date")
dfx = df.withColumn("rolling_amt",(sum(col("amount")).over(win)))
dfx.show()
