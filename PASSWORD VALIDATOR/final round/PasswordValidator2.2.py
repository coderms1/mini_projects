# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: Matthew Simone
# Due Date: 10/06/24

##THIS IS THE ONE!!!!!!!!!!!
#WITH comments

def validatePassword(firstName, lastName, sPassword):
    # Initialize & assign
    charCount = {}
    upperChar = False
    lowerChar = False
    digitChar = False
    specialChar = False
    specialChars = "!@#$%^"
    violations = []
    # Analyze sPassword in a loop
    for letter in sPassword:
        lowerLetter = letter.lower()
        # Check if lowerLetter is already in charCount
        if lowerLetter in charCount:
            charCount[lowerLetter] += 1  # Increment the count
        else:
            charCount[lowerLetter] = 1  # Initialize count to 1
        if letter.isupper():
            upperChar = True
        if letter.islower():
            lowerChar = True
        if letter.isdigit():
            digitChar = True
        if letter in specialChars:
            specialChar = True

    # Combine first initials
    initials = firstName[0] + lastName[0]

    # Validate sPassword
    #  rules
    if not (8 <= len(sPassword) <= 12):
        violations.append("Password must be between 8 and 12 characters.")
    if sPassword.lower().startswith("pass"):
        violations.append("Password can't start with Pass.")
    if not upperChar:
        violations.append("Password must contain at least 1 uppercase letter.")
    if not lowerChar:
        violations.append("Password must contain at least 1 lowercase letter.")
    if not digitChar:
        violations.append("Password must contain at least 1 number.")
    if not specialChar:
        violations.append("Password must contain at least 1 of these special characters ! @ # $ % ^")
    if initials.lower() in sPassword.lower():
        violations.append(f"Password must not contain user initials.")

    # Check for repeated characters
    duplicates = {letter: count for letter, count in charCount.items() if count > 1}
    if duplicates:
        violationMessage = "The following characters appear more than once:\n"
        for letter, count in duplicates.items():
            violationMessage += f"{letter}: {count} times\n"
        violations.append(violationMessage)
    # Output - pass/fail
    if violations:
        for violation in violations:
            print(violation)
            return False
    else:
        print("Password is valid and OK to use.")
        return True

def main():
    # Prompt user for their full name
    sUsername = input("Enter full name such as John Smith: ")
    spaceIndex = sUsername.find(" ")  # Find the index of the space
    # Ensure a valid full name is entered
    if spaceIndex == -1:
        print("Please enter both a first and last name.")
        return
    # Extract first and last names
    firstName = sUsername[:spaceIndex].strip()
    lastName = sUsername[spaceIndex + 1:].strip()
    while True:  # Loop until password is valid
        sPassword = input("Enter new password: ")
        isValid = validatePassword(firstName, lastName, sPassword)
        if isValid:
            break  
# Call the main function
main()