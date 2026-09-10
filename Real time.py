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
