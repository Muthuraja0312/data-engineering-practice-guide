# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

data1 = [
    (1, "A", "A", 1000000),
    (2, "B", "A", 2500000),
    (3, "C", "G", 500000),
    (4, "D", "G", 800000),
    (5, "E", "W", 9000000),
    (6, "F", "W", 2000000),
]
df1 = spark.createDataFrame(data1, ["emp_id", "name", "dept_id", "salary"])
df1.show()

data2 = [("A", "AZURE"), ("G", "GCP"), ("W", "AWS")]
df2 = spark.createDataFrame(data2, ["dept_id1", "dept_name"])
df2.show()

df1.createOrReplaceTempView("adf")
df2.createOrReplaceTempView("bdf")

df3=spark.sql(" select * from (select a.*,b.dept_name,dense_rank() over (partition by dept_name order by salary desc) as rn from adf a left join bdf b on a.dept_id = b.dept_id1) where rn =2; ")
#df3.show()

Winspce = Window.partitionBy("dept_name").orderBy(col("salary").desc())

dfa = df1.join(df2,col("dept_id") == col("dept_id1"),"left")
dfa.show()

dfb = dfa.withColumn("rank", dense_rank().over(Winspce))
dfb.filter("rank==2").show()
