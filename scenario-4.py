# Initialize Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()
from pyspark.sql.functions import *
from pyspark.sql.window import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CreateDF").getOrCreate()


from pyspark.sql import SparkSession

from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("VisitsTransactions").getOrCreate()


data = [(1, 5), (2, 6), (3, 5), (3, 6), (1, 6)]
df = spark.createDataFrame(data, ["customer_id", "product_key"])
df.show()
data2 = [(5,), (6,)]
df2 = spark.createDataFrame(data2, ["product_key"])
#df2.show()

df.createOrReplaceTempView("adf")
df2.createOrReplaceTempView("bdf")

dfz = spark.sql("select customer_id from adf where product_key in (select * from bdf) group by customer_id having count( distinct product_key) = (select count(*) from bdf)")
#dfz.show()

ddf = spark.sql("select customer_id from adf join bdf on adf.product_key = bdf.product_key group by customer_id having count( distinct adf.product_key) = (select count(*) from bdf)")
ddf.show()
# Count of required products
total_products = df2.count()

# Filter customers who bought only products in product list
dfl = df.join(df2, "product_key")
#dfl.show()
# Group and check if they bought all products
result = dfl.groupBy("customer_id") \
           .agg(countDistinct("product_key").alias("cnt")) \
           .where(col("cnt") == total_products) \
           .select("customer_id")

#result.show()
