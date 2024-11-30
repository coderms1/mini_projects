# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: Matthew Simone
# Due Date: 10/06/24

# THIS IS THE ONE!!!!!!!!!!!!

def isValidPassword(sName, sPassword):
    
    sInitials = sName[0] + sName[sName.find(" ") + 1]
    charCount = {}  
    specialChars = "!@#$%^"
    hasUpper = hasLower = hasDigit = hasSpecial = False
    validPassword = True  

    if len(sPassword) < 8 or len(sPassword) > 12:
        print("Password must be between 8 and 12 characters.")
        validPassword = False

    if sPassword.lower().startswith("pass"):
        print("Password can't start with 'Pass'.")
        validPassword = False

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
    if sInitials.lower() in sPassword.lower():
        print("Password must not contain user initials.")
        validPassword = False

    duplicates = ""
    for letter, count in charCount.items():
        if count > 1:
            duplicates += f"{letter}: {count} times\n"

    if duplicates:
        print("These characters appear more than once:")
        print(duplicates)
        validPassword = False
    if validPassword:
        print("Password is valid and OK to use.")
        return True
    else:
        return False

def main():
    sName = input("Enter full name such as John Smith: ").title()

    while True:
        sPassword = input("Enter new password: ")
        if sPassword == "":
            break
        elif isValidPassword(sName, sPassword):
            break
        else:
            continue

main()
