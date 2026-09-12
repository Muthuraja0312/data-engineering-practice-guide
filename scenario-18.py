Write a SQL query to calculate each employee’s experience from their date of joining up to today in the format years, months, and days 3yr 3month 2 days.

spark = SparkSession.builder \
    .appName("EmployeeExperience") \
    .getOrCreate()

data = [
    (101, "Alice", date(2018, 5, 10)),
    (102, "Bob", date(2020, 8, 25)),
    (103, "Charlie", date(2015, 1, 15)),
    (104, "David", date(2022, 11, 5)),
    (105, "Emma", date(2010, 3, 20))
]

schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("employee_name", StringType(), True),
    StructField("date_of_joining", DateType(), True)
])

df = spark.createDataFrame(data, schema)

df.show()
  
result = spark.sql("""
SELECT
    employee_id,
    employee_name,
    date_of_joining,

    TIMESTAMPDIFF(YEAR, date_of_joining, CURRENT_DATE()) AS years,

    TIMESTAMPDIFF(MONTH, date_of_joining, CURRENT_DATE()) % 12 AS months,

    DATEDIFF(
        CURRENT_DATE(),
        ADD_MONTHS(
            date_of_joining,
            TIMESTAMPDIFF(YEAR, date_of_joining, CURRENT_DATE()) * 12
            + TIMESTAMPDIFF(MONTH, date_of_joining, CURRENT_DATE()) % 12
        )
    ) AS days

FROM employees
""")

result.show()
