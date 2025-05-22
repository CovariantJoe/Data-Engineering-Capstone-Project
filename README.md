# Description of the Project
As part of the Capstone project, you will assume the role of an Associate Data Engineer who has recently joined an e-commerce organization. You will be presented with a business challenge that requires building a data platform for retailer data analytics.

## 📖 Table of Contents
- [Bussiness Scenario](#bussiness-scenario)
- [Project Objectives](#project-objectives)
- [Module 1 - MySQL OLTP System](#module-1)
- [Module 2 - MongoDB Inventory](#module-2)
- [Module 3 - PostgreSQL Warehouse](#module-3)
- [Module 4 - IBM Db2 & Cognos Analytics Dashboard](#module-4)
- [Module 5 - ETL Pipeline to Sync Databases](#module-5)
- [Module 6 - Spark Machine Learning Forecast](#module-6)

## Bussiness Scenario
SoftCart's online presence is primarily through its website, which customers access using a variety of devices like laptops, mobiles and tablets.
-  All the catalog data of the products is stored in the MongoDB NoSQL server.
- All the transactional data like inventory and sales are stored in the MySQL database server.
- Data is periodically extracted from these two databases and put into the staging data warehouse running on PostgreSQL. The production data warehouse is on the cloud instance of IBM DB2 server.
- BI teams connect to the IBM DB2 for operational dashboard creation. IBM Cognos Analytics is used to create dashboards.
- SoftCart uses Hadoop cluster as its big data platform where all the data is collected for analytics purposes.
- Spark is used to analyse the data on the Hadoop cluster.
- To move data between OLTP, NoSQL and the data warehouse, ETL pipelines are used and these run on Apache Airflow.

## Project Objectives
The Capstone project is divided into 6 Modules:
* In Module 1, you will design the OLTP database for an E-Commerce website, populate the OLTP Database with the data provided and automate the export of the daily incremental data into the data warehouse.
* In Module 2, you will set up a NoSQL database to store the catalogue data for an E-Commerce website, load the E-Commerce catalogue data into the NoSQL database, and query the E-Commerce catalogue data in the NoSQL database.
* In Module 3, you will design the schema for a data warehouse based on the schema of the OLTP and NoSQL databases. You’ll then create the schema and load the data into fact and dimension tables, automate the daily incremental data insertion into the data warehouse, and create Cubes and Rollups to make the reporting easier.
* In Module 4, you will create a Cognos data source that points to a data warehouse table, create a bar chart of Quarterly sales of cell phones, create a pie chart of sales of electronic goods by category, and create a line chart of total sales per month for the year 2020.
* In Module 5, you will extract data from OLTP, NoSQL, and MongoDB databases into CSV format. You will then transform the OLTP data to suit the data warehouse schema and then load the transformed data into the data warehouse. Finally, you will verify that the data is loaded properly.
* In the 6 and final Module, you will use your skills in Big Data Analytics to create a Spark connection to the data warehouse, and then deploy a machine learning model on SparkML for making sales projections.

## Module 1
### Description
Your company needs you to design a data platform that uses MySQL as an OLTP database. The OLTP database is generally used to handle everyday business transactions. The schema of an OLTP database is highly normalized so as to achieve a very low latency. To further improve the latency an OLTP database stores only the recent data like the last few week's data. 

### Solution
Connect to MySQL Command Line Interface and create the database.


![connect](Module%201/1.png)

Create the sales_data table, using engine InnoDB.


![create](Module%201/2.png)

Import the provided transaction history into the sales_data table, use PhPMyAdmin.


![import](Module%201/3.png)

Create an index on the timestamp to speed up queries, then show all the indices on the table


![create index](Module%201/6.png)


![show index](Module%201/7.png)

Writing a bash script to export the rows in the sales_data table to automate the export of daily incremental data into the data warehouse. This script can be executed daily by configuring cron to run it on the linux server.


![script](Module%201/8.png)

## Module 2
### Description
Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalogue data.

### Solution
Using mongoimport to load the provided inventory catalog to the mongo database. Then, connecting to the mongo shell (which is in a remote server) to confirm the catalog collection was created


![connect](Module%202/1.png)

Creating an index on the field "type" to make the future queries faster


![index create](Module%202/2.png)

Counting the number of entries, or documents, whose type is laptop


![count laptops](Module%202/3.png)

Simple query to count smart phones with 6 inches of screen size


![count 6-inch](Module%202/4.png)

Query to find the average screen size of smart phones.


![average screen](Module%202/5.png)

Using mongoexport to extract only the fields that are required (id, type, model) into a csv


![export](Module%202/6.png)

## Module 3
### Description
The company would like to create a data warehouse so that it can create reports like:
* Total sales per year per country
* Total sales per month per category
* Total sales per quarter per country
* Total sales per category per country
You will use your data warehousing skills to design and implement a data warehouse for the company. You will start your project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema.

### Solution
Using the ERD tool in pgAdmin, I designed the following star schema for the data warehouse:


![star schema](Module%203/1.png)

The schema is made of 4 dimension tables with details and a fact table. Hence, the schema is highly normalized. 
The corresponding SQL statements to create this schema are:


![schema sql](Module%203/2.png)

A simple query to see what the dimension table category looks like:


![sql query](Module%203/3.png)

With the created schema, the main production database in IBM Db2 cloud is populated with all the transactional data provided.


![db2 load](Module%203/4.png)

Query to analyze the total amount of sales grouping both by category type and country, using grouping sets.


![db2 grouping sets](Module%203/5.png)

Query to analyze the average sales by country and year, using a group by cube statement.


![db2 cube](Module%203/6.png)

SQL statement to create a materialized view (MQT) which shows the total sales by country every time it's updated.


![db2 mqt](Module%203/7.png)

## Module 4
### Description
Your company has finished setting up a data warehouse. Now you are assigned the responsibility to design a reporting dashboard that reflects the key metrics of the business.

### Solution
Load the sales data in the provided ecommerce.csv to IBM Db2 cloud in order to connect it to IBM Cognos Analytics seamlessly


![db2 load](Module%204/1.png)

Inspecting the data before analyzing.


![cognos inspect](Module%204/2.png)

Line chart of sales by month, noting the month with the most sales is the first one, followed by the least selling month immediately after.


![cognos line](Module%204/3.png)

Pie chart showing the share of sales by category, showing a major difference between electronics sales and music/ebooks.


![cognos pie](Module%204/4.png)

Bar chart showing the total sales by quarter.


![cognos bar](Module%204/5.png)

## Module 5
### Part 1 Description
Transactional data from the OLTP database (in this case MySQL) needs to be propagated to the Warehouse (PostgreSQL) on a frequent basis. This data movement can be automated using ETL processes. You will setup an ETL process using Python to extract new transactional data for each day from the MySQL database, transform it and then load it into the data warehouse. Automating this sync up will save you a lot of time and standardize your process.

### Part 1 Solution
Connecting and authenticating to the PostgreSQL database, and a simple function to get the last row ID and hence know how desyncronized the databases are.


![connect](Module%205/1.png)

Function to extract all the entries in the MySQL OLTP database that are newer than the last transaction saved in Postgres. The password is hard-coded only for simplicity but better practice is to read from an external file or prompt


![extract](Module%205/2.png)

The new records since the last backup are then inserted.


![load](Module%205/3.png)

### Part 2 Description
Our data platform includes a Big Data repository that is used for analytics using Machine Learning with Apache Spark. This Big Data repository gets data from several sources including the Data Warehouse and the Web Server log. As data from the web server log is logged, it needs to be added to the Big Data system on a frequent basis - making it an ideal process to automate using a data pipeline. You will create and run a DAG using Apache Airflow to extract daily data from the web server log, process it, and store it in a format to prepare it for loading into the Big Data platform.

### Part 2 Solution

Imports and setup of the Apache Airflow DAG


![import](Module%205/4.png)


![dag](Module%205/5.png)

Extract pipeline stage which uses shell operators to extract only IP addresses from the e-commerce web logs 


![extract](Module%205/6.png)

Transform pipeline stage to remove the IP 198.46.149.143 from the previously extracted logs.


![transform](Module%205/7.png)

Load pipeline stage to save the processed IP logs to a tar file.


![loading](Module%205/8.png)

Screenshots from Apache Airflow showing the pipeline active and the analysis after it ran successfully. The web log processing takes about 10 seconds.


![airflow1](Module%205/9.png)


![airflow2](Module%205/10.png)

## Module 6
### Description
You will perform a number of tasks to analyze search terms on the e-commerce web server:

You will work in Watson Studio within a Jupyter notebook to run your analysis against a CSV file containing the webserver data. You will load this file into a Spark data frame and print the results of your queries against this data set. You will then load a pre-trained sales forecasting model and use this to predict the sales for next year.

### Solution
Setup importing all the requirements from pyspark, execute findspark(), and create a spark session.


![importing](Module%206/1.png)

Download the data which contains the search terms clients have used in the e-commerce web server. Then, load the data into a spark dataframe and show the number of rows, columns, and the first 5 search terms.


![downloading](Module%206/2.png)

Using aggregation on the spark dataframe to find the top 5 most searched terms in the e-commerce platform


![top5](Module%206/3.png)

Import the linear regression model from spark machine learning, then load the pre-trained model. The function predict() was created in this assignment to transform the data provided into a format accepted by the pre-trained ML model, 
and lastly use it to predict the number of sales for 2023.


![predict](Module%206/4.png)
