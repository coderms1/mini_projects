# Assignment: Password Validator
# Class: CIT-117 ~ Python-2 with Prof C*
# Author: Matthew Simone
# Due Date: 10/06/24

# Function checks user entries (Name/Password) against requirements
def isValidPassword(sName, sPassword):
    
    # Initialize & assign [Thx to Mikey for the find() method!]
    sInitials = sName[0] + sName[sName.find(" ") + 1]
    charCount = {}  
    specialChars = "!@#$%^"
    hasUpper = hasLower = hasDigit = hasSpecial = False
    validPassword = True  

    # First two checks: length and does not start with 'pass' [startswith() method]
    if len(sPassword) < 8 or len(sPassword) > 12:
        print("Password must be between 8 and 12 characters.")
        validPassword = False
    if sPassword.lower().startswith("pass"):
        print("Password can't start with 'Pass'.")
        validPassword = False

    # For loop run through each char in password [Thx Prof C for the get() method!!]
    for char in sPassword:
        lowerchar = char.lower()
        charCount[lowerchar] = charCount.get(lowerchar, 0) + 1

        # Checks for required character types
        if char.isupper():
            hasUpper = True
        elif char.islower():
            hasLower = True
        elif char.isdigit():
            hasDigit = True
        elif char in specialChars:
            hasSpecial = True

    # Gives output based on result of checks
    if not hasUpper:
        print("Password must contain at least 1 uppercase char.")
        validPassword = False
    if not hasLower:
        print("Password must contain at least 1 lowercase char.")
        validPassword = False
    if not hasDigit:
        print("Password must contain at least 1 number.")
        validPassword = False
    if not hasSpecial:
        print("Password must contain at least 1 of these special characters ! @ # $ % ^")
        validPassword = False
    if sInitials.lower() in sPassword.lower():
        print(f"Password must not contain user initials: {sInitials} was used.")
        validPassword = False

    # Checks for duplicate characters/gives Output
    duplicates = ""
    for char, count in charCount.items():
        if count > 1:
            duplicates += f"{char}: {count} times\n"
    if duplicates:
        print("These characters appear more than once:")
        print(duplicates)
        validPassword = False
    # If passes all checks - Output
    if validPassword:
        print(f"Welcome {sName}!\nYour password is valid and OK to use!")
        #print("Password is valid and OK to use.")
        return True
    else:
        return False

# Main function that takes in user input (name & password)
def main():
    sName = input("Enter full name such as John Smith: ").title()

    # While loop to prompt or exit program
    while True:
        sPassword = input("Enter new password: ")
        if sPassword == "":
            break
        elif isValidPassword(sName, sPassword):
            break
        else:
            continue
# Call main function
main()
