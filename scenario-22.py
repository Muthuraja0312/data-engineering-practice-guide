data = [
    ('A', 'D', 'D'),
    ('B', 'A', 'A'),
    ('A', 'D', 'A')
]

dfa = spark.createDataFrame(data).toDF("TeamA", "TeamB", "Won")

dfa.show()

dfb = dfa.select(col("TeamA")).union(dfa.select(col("TeamB"))).distinct()
dfb.show()

dfc = dfa.groupBy("Won").count()
dfc.show()

dfd = dfb.join(dfc,dfb["TeamA"] == dfc["Won"],"full").drop("won")

dfe = dfd.withColumn("count", coalesce(col("count"), lit(0)))
dfe.show()
