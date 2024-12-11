# File: SQLdb_w_Py.py 

# Assignment: SQL DB Interact with Python
# Class: Python 2 w/ Prof C
# Author: Matthew Simone
# Due Date: 12/22/2024

import sqlite3
import csv

# Connect to the Database
dbConnection = sqlite3.connect("myDatabase.db")
cursor = dbConnection.cursor()

# CREATE TABLEs - try/except with customized error handling
try:
    sCreateTable = "CREATE TABLE Employee(EmployeeID INT, Name TEXT)"
    cursor.execute(sCreateTable)
    print(sCreateTable)
except sqlite3.OperationalError:
    print("Table 'Employee' already exists.")

try:
    sCreateTable = "CREATE TABLE Pay(EmployeeID INT, Year INT, Earnings REAL)"
    cursor.execute(sCreateTable)
    print(sCreateTable)
except sqlite3.OperationalError:
    print("Table 'Pay' already exists.")

try:
    sCreateTable = "CREATE TABLE SocialSecurityMinimum(Year INT, Minimum REAL)"
    cursor.execute(sCreateTable)
    print(sCreateTable)
except sqlite3.OperationalError:
    print("Table 'SocialSecurityMinimum' already exists.")

dbConnection.commit() # save it

# Insert data into Employee table
sInsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
sInsertEmployeeReset = sInsertEmployee
iRows = 0 

with open("Employee.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sInsertEmployee += f"{row[0]}, '{row[1]}')"
        print(sInsertEmployee)  # Print the SQL statement
        cursor.execute(sInsertEmployee)  # Execute the SQL statement
        sInsertEmployee = sInsertEmployeeReset  # Reset the query template
        iRows += 1  # Increment row counter

print(f"{iRows} Rows Inserted.\n")

# Insert data into Pay table
sInsertPay = "INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES("
sInsertPayReset = sInsertPay
iRows = 0  # Reset row counter

with open("Pay.txt", "r") as file:
    reader = csv.reader(file)
    next(reader) 

    for row in reader:
        sInsertPay += f"{row[0]}, {row[1]}, {row[2]})"
        print(sInsertPay) 
        cursor.execute(sInsertPay) 
        sInsertPay = sInsertPayReset
        iRows += 1

print(f"{iRows} Rows Inserted.\n")

# Insert data into SocialSecurityMinimum table
sInsertSocialSecurityMinimum = "INSERT INTO SocialSecurityMinimum(Year, Minimum) VALUES("
sInsertSocialSecurityMinimumReset = sInsertSocialSecurityMinimum
iRows = 0 

with open("SocialSecurityMinimum.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sInsertSocialSecurityMinimum += f"{row[0]}, {row[1]})"
        print(sInsertSocialSecurityMinimum)
        cursor.execute(sInsertSocialSecurityMinimum)
        sInsertSocialSecurityMinimum = sInsertSocialSecurityMinimumReset
        iRows += 1

print(f"{iRows} Rows Inserted.\n")

# Commit (save) the changes
dbConnection.commit()

# EXECUTE a SELECT statement using JOINS and ORDER them
cursor.execute("""
SELECT e.EmployeeID, e.Name, p.Year, p.Earnings, s.Minimum, 
    CASE 
        WHEN p.Earnings >= s.Minimum THEN 'Yes'
        ELSE 'No'
    END AS Eligible
FROM Employee e
JOIN Pay p ON e.EmployeeID = p.EmployeeID
JOIN SocialSecurityMinimum s ON p.Year = s.Year
ORDER BY e.EmployeeID, p.Year
""")

# Fetch all the results
results = cursor.fetchall()

# Print out the results in a structured list
print(f"{'EmployeeID':<12}{'Name':<20}{'Year':<6}{'Earnings':<12}{'Minimum':<10}{'Eligible'}")
print("-" * 70)
for row in results:
    print(f"{row[0]:<12}{row[1]:<20}{row[2]:<6}{row[3]:<12.2f}{row[4]:<10.2f}{row[5]}")

# Close it up!
dbConnection.close()