To find the customer who doesnt placed any order:

# Customers data
customers_data = [
    (1, "Will"),
    (2, "Jane"),
    (3, "Alex"),
    (4, "Bill")
]

# Orders data
orders_data = [
    (101, 1, 250.00),
    (102, 3, 300.00)
]

# Define schemas
customers_columns = ["customer_id", "customer_name"]
orders_columns = ["order_id", "customer_id", "amount"]

# Create DataFrames
df1 = spark.createDataFrame(customers_data, customers_columns)
df2 = spark.createDataFrame(orders_data, orders_columns)

df1.createOrReplaceTempView("df1")
df2.createOrReplaceTempView("df2")

#df = spark.sql("select a.* from df1 a left join df2 b on a.customer_id = b.customer_id where order_id is null")
#df.show()

df1.show()
df2.show()

df3 = df1.join(df2,["customer_id"],"left")
df4 = df3.filter(col("order_id").isNull()).select("customer_id","customer_name")

df4.show()
