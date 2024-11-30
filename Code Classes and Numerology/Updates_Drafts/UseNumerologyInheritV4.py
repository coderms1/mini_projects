# File: UseNumerologtyInheritV2.py

# Numerology with Inheritance
# Coder: zim

# import class from file
from NumerologyLifePathDetailsV4 import NumerologyLifePathDetailsV4

def main():
    # Step 1: Validate name input
    while True:
        sName = input("Enter your full name: ").strip()
        if sName:
            break
        print("Name cannot be empty. Please try again.")

    # Step 2: Validate DOB input
    while True:
        nDOB = input("Enter your date of birth (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        try:
            numerology = NumerologyLifePathDetailsV4(sName, nDOB)
            break
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Step 3: Display the results
    print("\n" + "=" * 40)
    print(numerology)
    print("=" * 40 + "\n")

# Step 1: Call the main function
main()