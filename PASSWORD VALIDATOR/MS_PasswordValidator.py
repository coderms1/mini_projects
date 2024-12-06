# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: msimone2301 (zim)
# Due Date: 10/06/24

def main():  
    # Step 2: Prompt the user for a valid full name until it is entered correctly
    while True:
        sName = input("Enter full name such as John Smith: ").title()
        if not sName:
            return
        elif len(sName.split()) == 2:
            break
        else:
            continue

    # Step 3: Extract user initials and define special characters after valid name is entered
    sInitials = sName[0] + sName[sName.find(" ") + 1]
    specialChars = "!@#$%^"

    # Step 4: Prompt the user for a password until valid (or exit)
    while True:
        sPassword = input("Enter new password: ")
        if not sPassword: 
            return

        # Step 5: Initialize & assign
        hasUpper = hasLower = hasDigit = hasSpecial = False
        charCount = {} 
        duplicates = ""
        validPassword = True

        # Step 6: Check password length and prohibit starting with pass
        if len(sPassword) not in range(8, 13):
            print("Password must be between 8 and 12 characters.")
            validPassword = False
        if sPassword.lower().startswith("pass"):
            print("Password can't start with Pass.")
            validPassword = False

        # Step 7: Check for required amounts/types of characters
        for letter in sPassword:
            lowerLetter = letter.lower()
            charCount[lowerLetter] = charCount.get(lowerLetter, 0) + 1
            if letter.isupper():
                hasUpper = True
            elif letter.islower():
                hasLower = True
            elif letter.isdigit():
                hasDigit = True
            elif letter in specialChars:
                hasSpecial = True

        # Step 8: Validate required character types
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

        # Step 9: Check for duplicates in a case-insensitive manner
        for char, count in charCount.items():
            if count > 1:
                duplicates += f"{char}: {count} times\n"
        if duplicates:
            print("These characters appear more than once:")
            print(duplicates)
            validPassword = False

        # Step 10: Check for user's initials
        if sInitials.lower() in sPassword.lower():
            print(f"Password must not contain user initials: {sInitials}")
            validPassword = False

        # Step #11: Final validation output: (password valid or continue to prompt)
        if validPassword:
            print("Password is valid and OK to use.")
            print(f"Welcome to the Matrix, {sName}!")
            break
        else:
            continue

main()  # Step 1: Start the program by calling the main function
