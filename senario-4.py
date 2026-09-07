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

sourcedata = [
      (1, "A"),
      (2, "B"),
      (3, "C"),
      (4, "D")]
mysourceshcema = ["id","name"]
sourcedf = spark.createDataFrame(sourcedata,schema=mysourceshcema)
sourcedf.show()

targetdata = [
      (1, "A"),
      (2, "B"),
      (4, "X"),
      (5, "F")]
mytargetschema = ["id1","name1"]
targetdf = spark.createDataFrame(targetdata,schema=mytargetschema)
targetdf.show()

sourcedf.createOrReplaceTempView("adf")
targetdf.createOrReplaceTempView("bdf")

df = spark.sql("select id,(case when name != name1 then 'Mismatch' when name is null then 'new in target' when name1 is null then 'new in source' end)as comment from (select coalesce(id,id1) as id, a.name, b.name1 from adf a full join bdf b on a.id = b.id1 where a.name != b.name1 or a.name is null or b.name1 is null)")
df.show()
