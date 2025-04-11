## Grade Analyzer ##
# Python 101 - Mini Projects
# Coder: zim

"""
This program prompts the user for a name and four test
    scores (as ints) and whether the user wants to drop
        the lowest test score in order to improve the overall
            average.  It then prints out the overall average as a
                float and the equivalent letter grade.
            We focus on the use of if/elif/else statements along
        with the use of both math and basic logic to determine the
    results while exiting the program with an error message if the
user inputs the incorrect data type or expected response.
"""

import sys # allows sys.exit

# Prompt for student's name
sStudent = input("Enter the student's name: ")

# Prompt for 4 test scores
print("Enter the 4 test scores:")
iTest1 = int(input("Test 1: "))
iTest2 = int(input("Test 2: "))
iTest3 = int(input("Test 3: "))
iTest4 = int(input("Test 4: "))

# Prompt to drop the lowest grade
sDropLowest = input("Drop the lowest grade? (Y/N): ").upper()

# Validate test scores (must be greater than 0)
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    sys.exit("Test scores must be greater than 0.")

# Validate user input (must be Y or N)
if sDropLowest == "Y":
    fDivisor = 3.0
    # Find the lowest grade
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        iLowTest = iTest1
    elif iTest2 <= iTest3 and iTest2 <= iTest4:
        iLowTest = iTest2
    elif iTest3 <= iTest4:
        iLowTest = iTest3
    else:
        iLowTest = iTest4
elif sDropLowest == "N":
    iLowTest = 0
    fDivisor = 4.0
else:
    sys.exit("Enter Y or N to Drop the Lowest Grade.")

# Calculate the average
fAverage = (iTest1 + iTest2 + iTest3 + iTest4) - iLowTest / fDivisor

# Process: Determine Letter Grade using Average
if fAverage >= 97.0:
    sLetterGrade = "A+"
elif fAverage >= 96.9:
    sLetterGrade = "A"
elif fAverage >= 90.0:
    sLetterGrade = "A-"
elif fAverage >= 87.0:
    sLetterGrade = "B="
elif fAverage >= 84.0:
    sLetterGrade = "B"
elif fAverage >= 80.0:
    sLetterGrade = "B-"
elif fAverage >= 77.0:
    sLetterGrade = "C+"
elif fAverage >= 74.0:
    sLetterGrade = "C"
elif fAverage >= 70.0:
    sLetterGrade = "C-"
elif fAverage >= 67.0:
    sLetterGrade = "D+"
elif fAverage >= 64.0:
    sLetterGrade = "D"
elif fAverage >= 60.0:
    sLetterGrade = "D-"
else:
    sLetterGrade = "F"

# Output: Display results to user
print(f"{sStudent}'s test average is: {fAverage:.1f}")
print(f"Letter grade for the test is: {sLetterGrade}")
