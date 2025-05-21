#!/bin/sh

# Simple script to backup the MySQL OLTP database. This will automate exporting the transactional
# data from the MySQL server to the other databases.

if mysqldump --user=root -p sales sales_data > sales_data.sql; then
echo "Export successful"
else
echo "Error exporting"
fi
