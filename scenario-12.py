# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

data = [(1,'Alice',25,'F'),(2,'Bob',40,'M'),(3,'Raj',46,'M'),(4,'Sekar',66,'M'),(5,'Jhon',47,'M'),(6,'Timoty',28,'M'),(7,'Brad',90,'M'),(8,'Rita',34,'F')]

df = spark.createDataFrame(data,['customer_id','name','age','gender'])
df.show()

df.createOrReplaceTempView("adf")

df1 = spark.sql("select age_grp,count(age_grp) as cnt from (select *, case when age between 19 and 35 then '19-35' when  age between 36 and 50 then '36-50' else '50+' end as age_grp from adf) group by age_grp ")
df1.show()
