data = [
    (101, "Eng", 90),
    (101, "Sci", 80),
    (101, "Mat", 95),
    (102, "Eng", 75),
    (102, "Sci", 85),
    (102, "Mat", 90)
]

columns = ["Id", "subject", "marks"]

df = spark.createDataFrame(data, columns)

df.show()

df.createOrReplaceTempView("adf")
df1 = spark.sql("select id, max(case when subject ='Eng' then marks end) as Eng, max(case when subject ='Sci' then marks end) as Sci,max(case when subject ='Mat' then marks end) as Mat from adf group by id ")
#df1.show()

df2 = df.groupBy("id").pivot("subject").agg(max(col("marks")))
df2.show()
