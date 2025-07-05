# Assignment: Numerology (submitted version)
# Class: Python-2 w/ Prof C *
# Author: sim
# Due Date: 11/17/2024
'''This is the first version of the UseNumerology class.
Completed on 11/17/2024.'''

# Import the Numerology class from Numerology file (technically step 1?)
from Numerology import Numerology

# Step 2: Define the main function
def main():
    # Step 3: Loop to validate name input
    while True:
        sName = input("Enter your full name: ").strip()
        if sName: 
            break
        print("Name cannot be empty. Please try again.")

    # Step 4: Prompt & Loop to validate DOB input (w/ error handling)
    while True:
        nDOB = input("Enter your date of birth (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        try:
            numerology = Numerology(sName, nDOB)
            break 
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Step 5: Display the results using __str__ method and neat formatting
    print("\n" + "=" * 40)
    print(numerology)
    print("=" * 40 + "\n")

# Step 1: Call the main function
main()
