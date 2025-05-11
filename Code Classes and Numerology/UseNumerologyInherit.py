#File: UseNumerologtyInherit.py

# Assignment: Numerology with Inheritance 
# Class: Python-2 w/ Prof C *
# Author: sim
# Due Date: 12/01/2024

# Import class from file
from NumerologyLifePathDetails import NumerologyLifePathDetails

def main():
    # Validate name input (Step 2)
    while True:
        sName = input("Enter your full name: ").strip()
        if sName:
            break
        print("Name cannot be empty. Please try again.")

    # Validate DOB input (Step 3)
    while True:
        nDOB = input("Enter your date of birth (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        try:
            numerology = NumerologyLifePathDetails(sName, nDOB)
            break
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Display the results (Step 4)
    print("\n" + "=" * 40)
    print(numerology)
    print("=" * 40 + "\n")

# Call the main function (Step 1)
main()
