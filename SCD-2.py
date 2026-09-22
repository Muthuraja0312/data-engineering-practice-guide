select * from DimCustomer;

select * from StgCustomer;

MERGE INTO DimCustomer AS d
USING StgCustomer AS s
ON d.CustomerID = s.CustomerID AND d.IsCurrent = 'Y'
WHEN MATCHED AND (d.City != s.City OR d.Email != s.Email)
  THEN UPDATE SET d.EndDate = CURRENT_DATE(), d.IsCurrent = 'N'
WHEN NOT MATCHED
  THEN INSERT (CustomerID, CustomerName, City, Email, EffectiveDate, EndDate, IsCurrent)
       VALUES (s.CustomerID, s.CustomerName, s.City, s.Email, CURRENT_DATE(), DATE('9999-12-31'), 'Y');
============================================================================================================

# Databricks notebook source
# Databricks notebook source
print("=====🔴🔴🔴🔴🔴== CELL 1 =======")


data = [
    (1, "Sai",   "Python",     30000, "ACTIVE"),
    (2, "Raj",   "Python",     32000, "ACTIVE"),
    (3, "John",  "Java",       28000, "ACTIVE"),
    (4, "Rita",  "Python",     31000, "ACTIVE"),
    (5, "Sam",   "Java",       29000, "ACTIVE"),
    (6, "Kiran", "Databricks", 33000, "ACTIVE"),
    (7, "Anu",   "Python",     27000, "ACTIVE"),
    (8, "Ram",   "Spark",      34000, "ACTIVE"),
    (9, "Priya", "Spark",      30000, "ACTIVE"),
    (10,"Vijay", "Databricks", 35000, "ACTIVE")
]

df = spark.createDataFrame(
    data,
    ["student_id", "name", "course", "fee", "status"]
)

df.write \
  .format("delta") \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .saveAsTable("students")

print("INITIAL DATA")
display(spark.table("students").orderBy("student_id"))


# COMMAND ----------

print("===🔴🔴🔴🔴🔴🔴==CELL 2======")

daily_data = [
    (2,  "Raj",   "Databricks", 45000, "ACTIVE"),
    (4,  "Rita",  "Spark",      42000, "ACTIVE"),
    (3,  "John",  "PySpark",    35000, "ACTIVE"),
    (11, "Rahul", "Python",     30000, "ACTIVE"),
    (12, "Sneha", "Databricks", 40000, "ACTIVE")
]

daily_df = spark.createDataFrame(
    daily_data,
    ["student_id", "name", "course", "fee", "status"]
)

daily_df.display()

# COMMAND ----------



print("===🔴🔴🔴🔴🔴==CELL 3======")

from delta.tables import DeltaTable

delta_table = DeltaTable.forName(spark, "students")


delta_table.alias("t").merge(

    daily_df.alias("s"),

            "t.student_id = s.student_id"
            
).whenMatchedUpdate(

    set={

        "name" : "s.name",
        "course" : "s.course",
        "fee" : "s.fee",
        "status" : "s.status"

    }

).whenNotMatchedInsert(

    values = {
        "student_id" : "s.student_id",
        "name" : "s.name",
        "course" : "s.course",
        "fee" : "s.fee",
        "status" : "s.status"

    }

).execute()


spark.table("students").orderBy("student_id").display()
