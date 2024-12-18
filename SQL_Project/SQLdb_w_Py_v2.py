# File: SQLdb_w_Py_v2.py **(Updated Version: Version 2.0)** 

# Assignment: SQL DB Interact with Python
# Class: Python 2 w/ Prof C
# Author: msimone2301 (zim)
# Due Date: 12/18/2024


# Unofficial first step - import the required modules
import sqlite3
import csv

# Step 1: Connect to the Database & SQLite DB File
dbConnection = sqlite3.connect("myDatabase.db")
cursor = dbConnection.cursor()

# Step 2: Function to Create Tables
def create_table(cursor, table_name, create_query):
    """
    CREATES TABLE in SQLite DB.

    Parameters:
        cursor (sqlite3.Cursor): executes SQL statements
        table_name (str): Name of table
        create_query (str): SQL query - creates table
    """
    try:
        cursor.execute(create_query)
        print(f"Table '{table_name}' created successfully.")
    except sqlite3.OperationalError:
        print(f"Table '{table_name}' already exists.")

# Step 3: Function to Insert Data into Tables
def insert_data_from_file(file_name, insert_query, cursor):
    """
    This function takes data from file & INSERTS it into the DB.

    Parameters:
        file_name (str): CSV file name
        insert_query (str): SQL query w/ placeholders (?) for data
        cursor (sqlite3.Cursor): DB cursor -> executes SQL statements
    """
    iRows = 0  # Row counter

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            # Ensure 'row' has the correct length for the query
            if len(row) != insert_query.count("?"):
                print(f"Skipping row {row} due to mismatch in column count.")
                continue

            cursor.execute(insert_query, row)  # Pass row data as a tuple
            iRows += 1  # Increment row counter

    print(f"{iRows} Rows Inserted into {file_name.split('.')[0]} table.\n")

# Step 2a-2c: Use the function to create the tables
create_table(cursor, "Employee", "CREATE TABLE Employee(EmployeeID INT, Name TEXT)")
create_table(cursor, "Pay", "CREATE TABLE Pay(EmployeeID INT, Year INT, Earnings REAL)")
create_table(cursor, "SocialSecurityMin", "CREATE TABLE SocialSecurityMin(Year INT, Minimum REAL)")

# Step 4: Insert Data into Tables
insert_data_from_file("Employee.txt", "INSERT INTO Employee(EmployeeID, Name) VALUES (?, ?)", cursor)
insert_data_from_file("Pay.txt", "INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES (?, ?, ?)", cursor)
insert_data_from_file("SocialSecurityMinimum.txt", "INSERT INTO SocialSecurityMin(Year, Minimum) VALUES (?, ?)", cursor)

# Step 5: Commit (save) the changes
dbConnection.commit()

# Step 6: EXECUTE a SELECT statement using JOINS and ORDER them
cursor.execute("""
SELECT e.EmployeeID, e.Name, p.Year, p.Earnings, s.Minimum, 
    CASE 
        WHEN p.Earnings >= s.Minimum THEN 'Yes'
        ELSE 'No'
    END AS Eligible
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMin s ON p.Year = s.Year
ORDER BY e.Name, p.Year
""")

# Step 7: Use the FETCH ALL method to get results
results = cursor.fetchall()

# Step 8: Print each list neatly & in order by Name & Year
print(f"{'Employee Name':<20}{'Year':<6}{'Earnings':>12}{'Minimum':>12}{'Eligible':>10}")
print("-" * 60)
for row in results:
    print(f"{row[1]:<20}{row[2]:<6}{row[3]:>12.2f}{row[4]:>12.2f}{row[5]:>6}")

# Step 9: Close it up!
dbConnection.close()
