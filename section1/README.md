# Data pipeline and airflow 

## [Airflow script](airflow_script.py)

This is a simple DAG with only one block called  process_applications_task.

Task is scheduled to run every hour (with cron expression "0 * * * *"), with 3 retries of 5 minute intervals.

## [Data Pipeline script (python)](pipeline.py)

Every hour, the data pipeline script checks the input folder for new raw files:
1. If new input raw files are found, the files are processed. The output files are created and separated into folders according to whether the application was successful (output_successful folder) or unsuccessful (output_unsuccessful folder). After processing, the raw files are moved into a processed_input folder so that they are not processed twice.
2. If no new raw input files are found, the script ends

Pipeline script behaviour:

|**Stage**|**Steps**|
|---|---|
|**Load**| Raw file is loaded into pandas dataframe|
|Clean and Validate|1. Create a temporary is_valid flag, initialised as True, to keep track of whether the memberships are valid<br>2. Name - for rows where name field is blank, change is_valid flag to False.<br>3. Mobile phone - remove whitespaces (assume that whitespaces does not affect validity of phone number). Check whether all characters are digits, and 8 digits in length - if false, change is_valid flag to False.<br> 4. Date of birth - raw data has varying formats. Change them all into python date format.<br> 5. above_18 flag - use python package 'relativedelta' to check whether the applicant's age is >=18 as of 2022-01-01. If yes, above_18 flag is True, otherwise False. If above_18 is False, then change is_valid flag is False.<br>6. email address - Assume that only email domains ending with .com and .net are valid, as per instructions (in reality, the other domains like .info and .biz are also valid). Use a regex pattern to verify whether the email is valid. If email is not valid, change is_valid to False.|
|**Create membership id** | Only for applications where is_valid is True, create the membership ID|
|**Save**|1. Drop the is_valid temporary column<br>2.Split the dataframe according to whether the application was valid, then save in output_successful or output_unsuccessful folder accordingly <br>3.Move the raw intput file into the input_processed folder|