from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("RunningTotal").getOrCreate()

data = [
    (101, 80, 90),
    (101, 70, 85),
    (101, 75, 80),
    (102, 60, 70),
    (102, 65, 75)
]

columns = ["student_id", "science_marks", "maths_marks"]

df = spark.createDataFrame(data, columns)

df.show()

win=Window.partitionBy("student_id").orderBy("science_marks")
win1=Window.partitionBy("student_id").orderBy("maths_marks")
df1=df.withColumn("running_sci", sum("science_marks").over(win))\
      .withColumn("running_maths", sum("maths_marks").over(win1))
df1.show()

df.createOrReplaceTempView("shd")
df1=spark.sql("select *, sum(maths_marks) over(partition by student_id order by maths_marks) as running_maths, sum(science_marks) over(partition by student_id order by science_marks) as running_science from shd order by student_id, running_maths,running_science")
df1.show()
=================================================
SQL:::
df.createOrReplaceTempView("sdf")
df=spark.sql(" select product_id,sum(sales_amount)as total from(select * from (select *, dense_rank() over(partition by product_id order by sales_month desc )as rnk  from sdf) where rnk<=3) group by product_id order by total desc limit 1" )
df.show()
