# Author: Matthew Simone // Due Date: 11/26/2023
# Class: CIT_115 // Teacher: Prof C
# Assignment: Grade Analyzer

# -Step 1: Import math operations
import math

# -Step 2: Acquire name of user
sName = str(input("Enter the person whose grades are being analyzed: "))

# -Step 3: Acquire the 4 test scores, one at a time
print("Enter your test scores: ")
iTest1 = int(input("Test #1: "))
iTest2 = int(input("Test #2: "))
iTest3 = int(input("Test #3: "))
iTest4 = int(input("Test #4: "))

# -Step 4: Make sure tests are within range 0-100
if iTest1 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
if iTest2 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
if iTest3 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit
if iTest4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

    
# -Step 5: Inquire if user wishes to drop a test and which test is the lowest
sDropLowest = str(input("Do you wish to drop your lowest grade? [Y or N]: "))
if sDropLowest == "Y" or "y":
    
    fDIVISOR = 3.0
    if   iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:
        iLOWEST = iTest1
    elif iTest2 < iTest3 and iTest2 < iTest4:
        iLOWEST = iTest2
    elif iTest3 < iTest4:
        iLOWEST = iTest3
    else:
        iLOWEST = iTest4
        
elif sDropLowest == "N" or "n":
   iLOWEST = 0
   fDIVISOR = 4.0
else:
    print("Must enter Y or N only.")
    raise SystemExit

# -Step 6: Assign 'new' value to final avg
iFinalTestAvg = (iTest1 + iTest2 + iTest3 + iTest4 - iLOWEST) / fDIVISOR


# -Step 7: Find letter grade average
if iFinalTestAvg >= 90:
    sLETTER_GRADE = 'A'
elif iFinalTestAvg >= 80 and iFinalTestAvg <= 89:
    sLETTER_GRADE = 'B'
elif iFinalTestAvg >= 70 and iFinalTestAvg >= 79:
    sLETTER_GRADE = 'C'
elif iFinalTestAvg >= 65 and iFinalTestAvg >= 69:
    sLETTER_GRADE = 'D'
else:
    sLETTER_GRADE = 'F'

# Step 8: Display results
print(sName + "'s Letter Grade is: " + sLETTER_GRADE)

print(iFinalTestAvg)
