# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

data = [(1,"Veg Biryani"),(2,"Veg Fried Rice"),(3,"Kaju Fried Rice"),(4,"Chicken Biryani"),(5,"Chicken Dum Biryani"),(6,"Prawns Biryani"),(7,"Fish Birayani")]

df1 = spark.createDataFrame(data,["food_id","food_item"])
df1.show()

ratings = [(1,5),(2,3),(3,4),(4,4),(5,5),(6,4),(7,4)]

df2 = spark.createDataFrame(ratings,["food_id","rating"])
df2.show()

df1.createOrReplaceTempView("adf")
df2.createOrReplaceTempView("bdf")

df= spark.sql("select a.*,b.rating,repeat('*',rating) as star from adf a left join bdf b on a.food_id = b.food_id")

df.show()

joindf = df1.join(df2,df1["food_id"]==df2["food_id"],"inner").select(df1["food_id"],"food_item","rating")
joindf.show()
finaldf = joindf.withColumn("stats(out of 5)",expr("repeat('*',rating)"))
finaldf.show()
