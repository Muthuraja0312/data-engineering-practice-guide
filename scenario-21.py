# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import *
from datetime import date
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("Sales") \
    .getOrCreate()
from datetime import date

data = [
    ("apple", "delhi", "view"),
    ("apple", "delhi", "click"),
    ("apple", "delhi", "click"),
    ("mango", "delhi", "order"),
    ("apple", "mumbai", "order"),
    ("mango", "delhi", "order"),
    ("apple", "mumbai", "order"),
    ("banana", "mumbai", "order"),
    ("apple", "mumbai", "order")
]

df = spark.createDataFrame(
    data,
    ["fruit", "customer_location", "action"]
)

df.show()

df.createOrReplaceTempView("adf")
dfa = df.filter(col("action")=="order")
dfb = dfa.groupBy("fruit","customer_location").agg(count(col("action")).alias("cnt"))
#dfb.show()
win = Window.partitionBy("customer_location").orderBy(col("cnt").desc())
dfc= dfb.withColumn("rnk",dense_rank().over(win)).filter("rnk==1")
dfc.show()
df1 = spark.sql("with cte as (select fruit,customer_location,count(fruit) as cnt from adf where action ='order' group by fruit,customer_location),cte2 as (select fruit,customer_location,dense_rank() over(partition by customer_location order by cnt desc)as rnk from cte) select * from cte2 where rnk=1 ")
#df1.show()
