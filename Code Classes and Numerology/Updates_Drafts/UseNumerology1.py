# File: UseNumerology1.py
# Coder: zim


from Numerology1 import Numerology1

def main():
    # Loop to validate name input
    while True:
        sName = input("Enter your full name: ").strip()
        if sName:
            break
        print("Name cannot be empty. Please try again.")

    # Loop to validate DOB input
    while True:
        nDOB = input("Enter your date of birth (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        try:
            numerology = Numerology1(sName, nDOB)
            break
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Display the results
    print("\n" + "=" * 40)
    print(numerology)
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()