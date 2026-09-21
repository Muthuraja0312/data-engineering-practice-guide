Fact Table: Orders
The fact table should capture measurable business events (transactions).
Typical columns:

order_id (PK, surrogate key)

customer_id (FK → Customers)

product_id (FK → Products)

shipping_id (FK → Shipping)

payment_id (FK → Payment)

order_date_id (FK → Date dimension)

quantity

unit_price

discount

total_revenue (derived: quantity × unit_price − discount)

👉 The fact table is numeric-heavy (measures like revenue, quantity) and links to dimensions via foreign keys.

📊 Dimension Tables
Customers → customer_id, name, address, demographics

Products → product_id, product_name, category, brand

Shipping → shipping_id, method, carrier, delivery_time

Payment → payment_id, mode, status

Inventory → stock_id, product_id, stock_available

Ratings → product_id, rating_value, review_text

Date → date_id, day, month, quarter, year

🌟 Why This Works
Star schema keeps dimensions denormalized → faster queries for BI dashboards.

Fact table focuses on metrics (revenue, quantity) → supports aggregations like top products per region, monthly sales trends, etc.

Dimensions provide descriptive context → who bought, what was bought, how it was shipped, how it was paid.

📌 Key Refinements
Add a Date dimension — critical for time-based analysis.

Store measures (quantity, revenue) in the fact table, not in dimensions.

Keep dimensions descriptive (attributes) and facts numeric (metrics).
