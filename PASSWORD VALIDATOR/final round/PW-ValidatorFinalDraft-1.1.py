# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: Matthew Simone
# Due Date: 10/06/24

# Function will check user entries (Name/Password) against specified requirements
def isValidPassword(sName, sPassword):
    
    # Step 4: Extract initials from the name
    sInitials = sName[0] + sName[sName.find(" ") + 1]

    # Step 12: Initialize variables for counting and character checks
    charCount = {}  
    specialChars = "!@#$%^"
    hasUpper = hasLower = hasDigit = hasSpecial = False
    validPassword = True  

    # Step 5: Check length and Step 6: Ensure it does not start with 'pass'
    if len(sPassword) < 8 or len(sPassword) > 12:
        print("Password must be between 8 and 12 characters.")
        validPassword = False
    if sPassword.lower().startswith("pass"):
        print("Password can't start with 'Pass'.")
        validPassword = False

    # Step 7-10: For loop to check each character in the password 
    for letter in sPassword:
        lowerLetter = letter.lower()
        charCount[lowerLetter] = charCount.get(lowerLetter, 0) + 1

        # Checks for required character types
        if letter.isupper():
            hasUpper = True
        elif letter.islower():
            hasLower = True
        elif letter.isdigit():
            hasDigit = True
        elif letter in specialChars:
            hasSpecial = True

    # Step 7-10: Output missing character types
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
        print("Password must contain at least 1 of these special characters ! @ # $ % ^")
        validPassword = False

    # Step 11: Check if password contains user initials
    if sInitials.lower() in sPassword.lower():
        print("Password must not contain user initials.")
        validPassword = False

    # Step 12: Check for duplicate characters
    duplicates = ""
    for letter, count in charCount.items():
        if count > 1:
            duplicates += f"{letter}: {count} times\n"
    if duplicates:
        print("These characters appear more than once:")
        print(duplicates)
        validPassword = False

    # Step 13: Final check and output if the password is valid
    if validPassword:
        print("Password is valid and OK to use.")
        return True
    else:
        return False

# Step 1: Main function that prompts user for their full name
def main():
  # Step 1: Prompt for full name with validation
  while True:
    # Step 1: Prompt for full name with validation
    sName = input("Enter full name such as John Smith: ").title()

    # Ensure a valid full name is entered (at least 2 words)
    if len(sName.split()) < 2:
      continue
    elif sName == "":
      break
    # Step 2: Prompt for the password after a valid name is entered
    sPassword = input("Enter new password: ")

    # Exit if the user presses Enter without typing a password
    if sPassword == "":
      break

    # Validate the entered password
    if isValidPassword(sName, sPassword):
      break
    else:
      continue

# Step 14: Call main function to start the program
main()