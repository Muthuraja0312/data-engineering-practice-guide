select dept,count(dept) as total from table group by dept;

df = df.groupBy("dept").agg(count(col("dept")).alias("total"))
df.show()

select *,(telugu+english+maths+science+social) as total from table;

df1 = df.withColumn("Total",(telugu+english+maths+science+social))
df1.show()
