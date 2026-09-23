# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import *
from datetime import date
from pyspark.sql.types import *
from pyspark.sql.types import StructType, StructField, IntegerType, DateType, DoubleType

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DateType, DoubleType
from datetime import date

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FinancialTransactions").getOrCreate()

data = [
    (1, "2024-01-15", 56.00, "Debit"),
    (2, "2024-01-15", 23.00, "Credit"),
    (3, "2024-01-15", 880.00, "Credit"),
    (4, "2024-01-15", 76.00, "Debit"),
    (5, "2024-01-16", 60.00, "Credit"),
    (6, "2024-01-16", 146.00, "Debit")
]

columns = [
    "TransactionID",
    "TransactionDate",
    "Amount",
    "TransactionType"
]

df = spark.createDataFrame(data, columns)

df.show()

df.createOrReplaceTempView("adf")

df1 = spark.sql("select transactionDate,credit - debit as balance from (select transactionDate,sum(case when TransactionType='Credit' then amount end) as credit,sum(case when TransactionType='Debit' then amount end) as debit from adf group by TransactionDate)")
#df1.show()
dfa = df.filter(col("TransactionType")=="Credit")
dfb=dfa.groupBy("TransactionDate").agg(sum(col("Amount")).alias("Credit"))
dfb.show()

dfc = df.filter(col("TransactionType")=="Debit")
dfd=dfc.groupBy("TransactionDate").agg(sum(col("Amount")).alias("Debit"))
dfd.show()

dfz = dfb.join(dfd,"TransactionDate").withColumn("balance",expr("Credit - Debit"))
dfz.drop("Credit","Debit").show()


from pyspark.sql.functions import sum, when, col

result = (
    df.groupBy("TransactionDate")
      .agg(
          sum(when(col("TransactionType") == "Credit", col("Amount"))
              .otherwise(0)).alias("Credit"),
          sum(when(col("TransactionType") == "Debit", col("Amount"))
              .otherwise(0)).alias("Debit")
      )
      .withColumn("Balance", col("Credit") - col("Debit"))
      .select("TransactionDate", "Balance")
)

result.show()
