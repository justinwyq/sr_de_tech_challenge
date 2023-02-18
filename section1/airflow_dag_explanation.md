# Data pipeline and airflow 

## Airflow script

Airflow is a simple DAG with only one block called the process_applications_task.

Task is scheduled to run every hour (with cron expression "0 * * * *"), with 3 retries of 5 minute interval.

## Data Pipeline script (python)

Every hour, the data pipeline script checks the input folder for new raw files, processes them and creates the output files, and then moves the raw files into a processed_input folder.

Additional comments are inserted into the script to explain the behaviour.