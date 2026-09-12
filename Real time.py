1.How did you reduce the runtime of an Airflow pipeline?

"In one of my projects, our DAG was taking ~2 hours. I reduced runtime by parallelizing independent tasks, switching from PythonOperator to 
SparkSubmitOperator so heavy transformations ran on Spark instead of Airflow workers, 
and pruning unnecessary dependencies. I also disabled catchup to avoid backfilling old runs. 
These changes cut runtime to ~40 minutes and improved reliability."

2.how do you reduce operational cost?
"Operational cost refers to the ongoing expense of running pipelines — compute, storage, and maintenance. In one project, we reduced costs by switching from CSV to 
Parquet (cut storage by 60%), partitioning BigQuery tables to scan less data, and moving cold data to cheaper storage tiers. We also made the pipeline event‑driven 
instead of hourly, which eliminated unnecessary runs.
Together, these changes reduced monthly cloud spend by ~40% while keeping SLAs intact."

3.\* If you have a 4-core worker node and a 1GB file with 8 partitions, how many tasks will run in parallel?
"For a 1 GB file split into 8 partitions, Spark will create 8 tasks. On a 4‑core worker node, 4 tasks can run in parallel, and the other 4 will run in the next wave.
So the job completes in 2 waves. 
In Spark, parallelism is determined by the number of partitions and available cores — each partition is one task, and tasks run on cores."

===========================================================================================================================
4. Spark — 50 GB file
* Columns: country_id, sales_amount, product_id, date
* Business reads country-level data only
* 70% data belongs to one country

How would you process this efficiently?
Since business queries are country-centric, I would store the data partitioned by country_id to enable partition pruning.
However, because 70% of the records belong to a single country, partitioning only by country would create severe data skew.
To solve this, I'd further partition the hot country using date or a salting strategy, store the data in Parquet format,
and size partitions around 128-256 MB. This reduces scan volume, improves parallelism, and prevents one executor from
processing most of the workload.
================================================================================================================
5. Spark — Jobs, Stages & Tasks
For eg:
df.filter()
df.groupBy()
df.show()
How many jobs, stages and tasks will be created?
Action          => New Job
Shuffle         => New Stage
Partition       => Task
1 Action -> 1 Job
1 Shuffle -> 2 Stages
#Partitions -> #Tasks
eg 2:
df.filter(...)
.groupBy(...)
.sum(...),count()
.show()
df.count() -- how many jobs, tasks, stages?
Job 1 = 2 stages
Job 2 = 1 stage
Total = 3 stages
YOUR CODE
                       │
          ┌────────────┴────────────┐
          │                         │
        show()                    count()
          │                         │
        Job 1                     Job 2
          │                         │
     ┌────┴────┐                    │
     │         │                    │
  Stage 1   Stage 2              Stage 1
     │         │                    │
 filter      final               count
 groupBy     aggregation(sum,count) partial
 aggregation(groupBy)
     │
   SHUFFLE(stage 2 starts)
  ===================================================================================================================
  6. Spark — Schema Handling
200-column CSV/Parquet file, but only 10 columns are required.
Source team is unreliable and may not follow the schema. Business wants missing/invalid columns to be read as NULL.
How would you handle this?
  df.withColumn("country_id", lit(None).cast("string"))
   Since only 10 out of 200 columns are needed, I would avoid reading the full schema and use column pruning, especially for Parquet. I'd maintain an expected schema for the 10 business columns, dynamically add any missing columns as NULL, and safely cast datatypes so invalid values become NULL instead of causing job failures. I would also log missing columns and invalid records to a data quality table for monitoring. This makes the pipeline resilient to schema drift while meeting the business requirement that missing or invalid columns be represented as NULL
==============================================================================================
7.4. AWS Glue + Spark
Job processes 10–100 GB of data. Assume G.2X workers.
What would you do on the Spark and Glue side to optimize performance and cost?
For a 10-100 GB Glue job using G.2X workers, I would store data in Parquet, read only required columns, use partition pruning, enable AQE, broadcast small lookup tables, minimize shuffles, and tune partition counts for 128-256 MB partition sizes. On the Glue side, I would enable autoscaling, use job bookmarks for incremental processing, and coalesce output files to avoid small-file issues. These optimizations reduce execution time, memory pressure, S3 I/O, and overall Glue cost
  ==========================================================================================================
                                                                                                                                                                                                                                                                                                       





