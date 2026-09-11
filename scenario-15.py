
from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("SecondHighestSalary").getOrCreate()

# Sample data
data = [
    ("HR", 101, 5000),
    ("HR", 102, 7000),
    ("HR", 103, 7000),  # tie
    ("HR", 104, 6000),
    ("HR", 105, 8000),

    ("Finance", 201, 9000),
    ("Finance", 202, 8500),
    ("Finance", 203, 9500),
    ("Finance", 204, 9500),  # tie
    ("Finance", 205, 7000),

    ("IT", 301, 10000),
    ("IT", 302, 9500),
    ("IT", 303, 8500),
    ("IT", 304, 9500),  # tie
    ("IT", 305, 8000)
]

# Define schema
columns = ["department", "employee_id", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)
#df.show()

df.createOrReplaceTempView("cdf")

df1 = spark.sql("select department,employee_id,salary,rn from (select *,dense_rank() over (partition by department order by salary desc) as rn from cdf) where rn=2")

df1.show()


windowdf = Window.partitionBy(col("department")).orderBy(col("salary").desc())

df1 = df.withColumn("rank", dense_rank().over(windowdf)).filter("rank==2").drop("rank")
