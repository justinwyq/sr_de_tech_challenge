# Submission for Govtech Senior Data Engineer Tech Challenge

Justin Wong's solution files for Govtech's [Senior Data Engineer Tech Challenge](https://github.com/ameeraadam/Senior-DE-Tech-Challenge).


|Section|Solution files|
|---|---|
|1|1. [README.md](section1/README.md) which provides documentation on the airflow script<br>2. [airflow_script.py](section1/airflow_script.py) - airflow script to schedule the pipeline to run every hour <br>3. [pipeline.py](section1/pipeline.py) - data pipeline script <br>4. [data](section1/data/) subfolder|
|2|1. [section2_erd.drawio.png](section2/section2_erd.drawio.png) - entity relationship diagram of the proposed database design<br>2. [Dockerfile](section2/Dockerfile) - dockerfile to set up the postgre database and run the DDL statements to create the tables<br>3. SQL files ([create_applications.sql](section2/create_applications.sql), [create_items.sql](section2/create_items.sql), [create_memberships.sql](section2/create_memberships.sql), [create_transaction_items.sql](section2/create_transaction_items.sql), [create_transactions.sql](section2/create_transactions.sql)) - these files contain the DDL statements to create the tables, and are copied into the docker container by the dockerfile<br> 4. [queries](section2/queries/) subfolder - contains the two SQL queries ([top_10_members.sql](section2/queries/top_10_members.sql), [top_3_items.sql](section2/queries/top_3_items.sql)) to get the top 10 members by spending, and top 3 items frequently bought by members|
|3|1. [README.md](section3/README.md) - markdown file containing solutions to design 1<br>2. [design2.png](section3/design2.png) - the proposed architecture for design 2, with comments about design decisions.|
|4|1. [Section 4 Explanatory Notes.pptx](section4/Section%204%20Explanatory%20Notes.pptx) - contains the screenshots and explanatory notes for the covid 19 dashboard <br> 2. [sg_covid_case_dashboard.pbix](section4/sg_covid_case_dashboard.pbix) - Power BI dashboard that will automatically load the data from API and generate the dashboard|
|5|1. [section5.ipynb](section5/section5.ipynb) - contains a jupyter notebook with the python script for predicting the buying price|
