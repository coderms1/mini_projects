# File: SQLdb_w_Py.py 

# Assignment: SQL DB Interact with Python
# Class: Python 2 w/ Prof C
# Author: msimone2301 (zim)
# Due Date: 12/22/2024

# Unofficial first step - import the required modules
import sqlite3
import csv

# Step 1: Connect to the Database & SQLite DB File
dbConnection = sqlite3.connect("myDatabase.db")
cursor = dbConnection.cursor()

# Step 2a: CREATE employee TABLE - try/except with customized error handling
try:
    sCreateTable = "CREATE TABLE Employee(EmployeeID INT, Name TEXT)"
    cursor.execute(sCreateTable)
    print(sCreateTable)
except sqlite3.OperationalError:
    print("Table 'Employee' already exists.")

# Step 2b: CREATE pay TABLE
try:
    sCreateTable = "CREATE TABLE Pay(EmployeeID INT, Year INT, Earnings REAL)"
    cursor.execute(sCreateTable)
    print(sCreateTable)
except sqlite3.OperationalError:
    print("Table 'Pay' already exists.")

# Step 2c: CREATE socialsecurityminimum TABLE
try:
    sCreateTable = "CREATE TABLE SocialSecurityMin(Year INT, Minimum REAL)"
    cursor.execute(sCreateTable)
    print(sCreateTable)
except sqlite3.OperationalError:
    print("Table 'SocialSecurityMin' already exists.")

# Step 3: Save tables to DB
dbConnection.commit() 

# Step 4a: INSERT data INTO employee table (iRows counter initialized)
sInsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
sInsertEmployeeReset = sInsertEmployee
iRows = 0 

with open("Employee.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sInsertEmployee += f"{row[0]}, '{row[1]}')"
        print(sInsertEmployee)  # Prints SQL statement
        cursor.execute(sInsertEmployee)  # Executes SQL statement
        sInsertEmployee = sInsertEmployeeReset  # Resets the query
        iRows += 1  # Increment 

print(f"{iRows} Rows Inserted.\n")

# Step 4b: Insert data into Pay table
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

# Step 4c: Insert data into SocialSecurityMinimum table
sInsertSocialSecurityMinimum = "INSERT INTO SocialSecurityMin(Year, Minimum) VALUES("
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

# Side step: Display the amount of data inserted (because it's cool 8-})
print(f"{iRows} Rows Inserted.\n")

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

# Step 8: Print each list neatly & in order by EmpID & Year
print(f"{'Employee Name':<20}{'Year':<6}{'Earnings':>12}{'Minimum':>12}{'Eligible':>10}")
print("-" * 60)
for row in results:
    print(f"{row[1]:<20}{row[2]:<6}{row[3]:>12.2f}{row[4]:>12.2f}{row[5]:>6}")

# Step 9: Close it up!
dbConnection.close()
