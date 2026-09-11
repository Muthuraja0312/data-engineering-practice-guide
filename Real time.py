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
