# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import max, col

spark = SparkSession.builder.appName("SalaryDiff").getOrCreate()

# Sample data
data = [
    (1, "Alice", "IT", 5000),
    (2, "Bob", "IT", 6000),
    (3, "Carol", "HR", 4500),
    (4, "David", "HR", 5500),
    (5, "Emma", "Sales", 7000)
]

columns = ["emp_id", "name", "dept", "salary"]

df = spark.createDataFrame(data, columns)

df.show()

df.createOrReplaceTempView("adf")

df1= spark.sql("select *,(max(salary) over (partition by dept order by salary desc)) - salary  as diff from adf order by emp_id")
#df1.show()
win = Window.partitionBy("dept").orderBy(col("salary").desc())
dfa = df.withColumn("max_sal",max(col("salary")).over(win))
dfb = dfa.withColumn("diff",col("max_sal") -col("salary") )
dfb.orderBy("emp_id").show()
