1.Liquid Clustering:
     in Delta Lake is a storage optimization technique that replaces partitioning and ZORDER. It clusters data dynamically based on chosen keys,
supports redefining keys without rewriting data, and adapts to skew and changing query patterns. It’s enabled with CLUSTER BY during table creation, and 
Databricks manages optimization automatically. 
Compared to partitioning, it’s more flexible and efficient for high‑cardinality, fast‑growing, or streaming datasets."
=========================================================================================================================
Partition Pruning -> Skip folders
Predicate Pushdown -> Skip rows
Column Pruning -> Skip unnecessary columns in Spark plan
Projection Pushdown -> Skip unnecessary columns at storage read

Partition pruning reduces partitions scanned, predicate pushdown reduces rows scanned, column pruning removes unused columns from Spark's execution plan, and projection pushdown ensures only those required columns are physically read from the source.
