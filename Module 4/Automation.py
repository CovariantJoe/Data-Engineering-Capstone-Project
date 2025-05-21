# This script extracts data from the MySQL server and, if they are new, saves them to the PostgreSQL server, according to the data architecture of the bussiness case study.
# The scripts allows this process to be automated. 
# Passwords are hard-coded for simplicity, in real life cases it is important to read them from an external text file instead.

PASSWORD_POSTGRES = 'NKhflhZqwp2oYrVOYINUJRto' 
PASSWORD_MYSQL = 'ccsVWrK1gYYo2iUjcoxao1Hw'

# Connect to MySQL
import mysql.connector

# Connect to PostgreSql

import psycopg2
dsn_hostname = '172.21.6.33'
dsn_user='postgres'        
dsn_pwd = PASSWORD_POSTGRES
dsn_port ="5432" 
dsn_database ="postgres"  


# create connection

conn = psycopg2.connect(
   database=dsn_database, 
   user=dsn_user,
   password=dsn_pwd,
   host=dsn_hostname, 
   port= dsn_port
)
cursor = conn.cursor()

def get_last_rowid():
    query = "SELECT * FROM sales_data ORDER BY rowid DESC LIMIT 1;"
    cursor.execute(query)
    return cursor.fetchall()[0][0]


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records returns a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.
def get_latest_records(rowid):
    query = "SELECT * FROM sales_data WHERE rowid > " + str(rowid) + ";"
    connectionMYSQL = mysql.connector.connect(user='root', password=PASSWORD_MYSQL,host='172.21.119.8',database='sales')
    cursorMYSQL = connectionMYSQL.cursor()
    execute = cursorMYSQL.execute(query)
    rows = cursorMYSQL.fetchall()
    connectionMYSQL.close()
    return rows

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into PostgreSql data warehouse.
# The function insert_records inserts all the records passed to it into the sales_data table in PostgreSql.
def insert_records(records):
    base = "INSERT INTO sales_data (rowid, product_id, customer_id, quantity)"
    for row in records:
        query = base + " values(%s,%s,%s,%s)"
        cursor.execute(query,row)
        conn.commit()
    conn.close()
    return

insert_records(new_records)
print("New rows inserted into production data warehouse = ", len(new_records))
