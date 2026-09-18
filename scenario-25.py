from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

data = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 1),
    (6, 2),
    (7, 2)
]

df = spark.createDataFrame(data, ['id', 'num'])

df.show()

df.createOrReplaceTempView("adf")

df1 = spark.sql("select num from (select num,lead(num,1) over (order by id) as first,lead(num,2) over (order by id) as second from adf) where num =first and num=second ")
df1.show()
