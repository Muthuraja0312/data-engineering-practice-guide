# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

#Create a new datafrane df1 with the given values
#Count null entries in a datafarme
#Remove null entries and the store the null entries in a new datafarme df2
#Create a new dataframe df3 with the given values and join the two dataframes df1 & df2
#Fill the null values with the mean age all of students
#Filter the students who are 18 years above and older

data = [('2020-05-30','Headphone'),('2020-06-01','Pencil'),('2020-06-02','Mask'),('2020-05-30','Basketball'),('2020-06-01','Book'),('2020-06-02','Mask'),('2020-05-30','T-Shirt')]
columns = ["sell_date",'product']

df = spark.createDataFrame(data,schema=columns)
df.show()

df.createOrReplaceTempView("adf")
df1 = spark.sql("select sell_date,collect_list(product) as product,size(collect_list(product)) as cnt from adf group by sell_date")
df1.show()

dfx = df.groupBy("sell_date").agg(collect_list(col("product")).alias("product"),size(collect_list(col("product"))).alias("cnt"))
dfx.show()
