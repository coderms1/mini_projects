# File: UseNumerologyInheritV3.py

# Assignment: Numerology with Inheritance 
# Class: Python-2 w/ Prof C *
# Author: Matthew Simone
# Due Date: 12/01/2024

# Import the Numerology class from Numerology.py
from NumerologyLifePathDetailsV2 import NumerologyLifePathDetailsV2

# Main function: gets user input & displays results
def main():
    # Loop: validate name input
    while True:
        sName = input("Enter your full name: ").strip()
        if sName:
            break
        print("Name cannot be empty. Please try again.")

    # Loop: validate DOB input
    while True:
        nDOB = input("Enter your date of birth (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        try:
            numerology = NumerologyLifePathDetailsV2(sName, nDOB)
            break
        except ValueError as error:
            print(f"Input error: {error}. Please try again.")

    # Display the results
    print("\n" + "=" * 40)
    print(numerology)
    print("=" * 40 + "\n")

# Call the main function
main()