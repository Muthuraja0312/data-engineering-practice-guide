# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

data = [('c00dac11bde74750b4d207b9c182a85f', 'Alex Thomas', 9),('eb6f2d3426694667ae3e79d6274114a4', 'Chris Gray', 2),('3f7b5b8e835d4e1c8b3e12e964a741f3', 'Emily Johnson', 4),('9a345b079d9f4d3cafb2d4c11d20f8ce', 'Michael Brown', 6),('e0a5f57516024de2a231d09de2cbe9d1', 'Jessica Wilson', 3)]

familydf = spark.createDataFrame(data,["id","name","family_size"])
familydf.show()

countrydata = [('023fd23615bd4ff4b2ae0a13ed7efec9', 'Bolivia', 2 , 4),('be247f73de0f4b2d810367cb26941fb9', 'Cook Islands', 4,8),('3e85ab80a6f84ef3b9068b21dbcc54b3', 'Brazil', 4,7),('e571e164152c4f7c8413e2734f67b146', 'Australia', 5,9),('f35a7bb7d44342f7a8a42a53115294a8', 'Canada', 3,5),('a1b5a4b5fc5f46f891d9040566a78f27', 'Japan', 10,12)]

countrydf = spark.createDataFrame(countrydata,["id","name","min_size","max_size"])
countrydf.show()

familydf.createOrReplaceTempView("adf")
countrydf.createOrReplaceTempView("bdf")

df = spark.sql("select name, max(no_of_county) as max from(select a.name,count(family_size) as no_of_county from adf a join bdf b on family_size between min_size and max_size group by a.name ) group by name order by max desc limit 1")
df.show()

dfx = familydf.alias("a").join(countrydf.alias("b"),(col("family_size") >=col("min_size")) & (col("family_size")  <=col("max_size"))).select("a.name","min_size","max_size")
dfy = dfx.groupBy("name").agg(count('*').alias("no_of_countries")).orderBy(col("no_of_countries").desc())
dfy.limit(1).show()
