# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: Matthew Simone
# Due Date: 10/06/24

# Function: isValidPassword()
# Description: This function checks the validity of a password against specific criteria,
# such as length, character types, and absence of user initials.

#THIS IS THE SECOND ONE!!!!!!!!!!


def isValidPassword(strName, strPassword):
    # Extract the initials from the user's full name
    strInitials = strName[0] + strName[strName.find(" ") + 1]
    dictCharCount = {}  # Dictionary to track character occurrences
    specialChars = "!@#$%^"
    hasUpper = hasLower = hasDigit = hasSpecial = False
    validPassword = True  # Flag to indicate overall password validity

    # Step 5: Check password length
    if len(strPassword) < 8 or len(strPassword) > 12:
        print("Password must be between 8 and 12 characters.")
        validPassword = False

    # Step 6: Check if the password starts with "Pass"
    if strPassword.lower().startswith("pass"):
        print("Password can't start with 'Pass'.")
        validPassword = False

    # Analyze each character in the password
    for letter in strPassword:
        lowerLetter = letter.lower()
        dictCharCount[lowerLetter] = dictCharCount.get(lowerLetter, 0) + 1

        # Set flags based on character types
        if letter.isupper():
            hasUpper = True
        elif letter.islower():
            hasLower = True
        elif letter.isdigit():
            hasDigit = True
        elif letter in specialChars:
            hasSpecial = True

    # Step 7-10: Check for each required character type
    if not hasUpper:
        print("Password must contain at least 1 uppercase letter.")
        validPassword = False
    if not hasLower:
        print("Password must contain at least 1 lowercase letter.")
        validPassword = False
    if not hasDigit:
        print("Password must contain at least 1 number.")
        validPassword = False
    if not hasSpecial:
        print("Password must contain at least 1 special character (! @ # $ % ^).")
        validPassword = False

    # Step 11: Check if the password contains the user's initials
    if strInitials.lower() in strPassword.lower():
        print(f"Password must not contain user initials ({strInitials}).")
        validPassword = False

    # Step 12: Check for repeated characters and print details
    repeatedCharacters = ""
    for letter, count in dictCharCount.items():
        if count > 1:
            repeatedCharacters += f"{letter}: {count} times\n"

    if repeatedCharacters:
        print("These characters appear more than once:")
        print(repeatedCharacters)
        validPassword = False

    # Final result of validation
    if validPassword:
        print("Password is valid and OK to use.")
        return True
    else:
        return False

# Function: main()
# Description: Orchestrates the flow of the program by taking user input and validating the password.
def main():
    # Step 1: Prompt the user for their first and last name and format it correctly
    strName = input("Enter your full name (e.g., John Smith): ").title()

    # Step 2: Loop until a valid password is entered or the user presses Enter to exit
    while True:
        strPassword = input("Enter a new password (or press Enter to exit): ")
        if strPassword == "":
            print("No password entered. Exiting the program.")
            break
        elif isValidPassword(strName, strPassword):
            print(f"Welcome, {strName}!")
            break
        else:
            print("Password validation failed. Please try again.")

# Entry point of the program
main()
