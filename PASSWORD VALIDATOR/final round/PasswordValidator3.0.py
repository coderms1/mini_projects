# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: Matthew Simone
# Due Date: 10/06/24

def extractAndValidatePassword(firstName, lastName, password):
    """
    This function validates the password based on the extracted first and last names.
    """
    # Initialize variables
    charCount = {}
    upperChar, lowerChar, digitChar, specialChar = False, False, False, False
    specialChars = "!@#$%^"
    violations = []
    
    # Analyze password characteristics in one loop
    for letter in password:
        lowerLetter = letter.lower()
        charCount[lowerLetter] = charCount.get(lowerLetter, 0) + 1
        
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

    # Validate password rules
    if not (8 <= len(password) <= 12):
        violations.append("Password must be between 8 and 12 characters.")
    if password.lower().startswith("pass"):
        violations.append("Password can't start with 'Pass'.")
    if not upperChar:
        violations.append("Password must contain at least 1 uppercase letter.")
    if not lowerChar:
        violations.append("Password must contain at least 1 lowercase letter.")
    if not digitChar:
        violations.append("Password must contain at least 1 number.")
    if not specialChar:
        violations.append("Password must contain at least 1 special character (!@#$%^).")
    if initials.lower() in password.lower():
        violations.append(f"Password must not contain user initials: {initials}.")

    # Check for repeated characters
    duplicates = {letter: count for letter, count in charCount.items() if count > 1}
    if duplicates:
        violationMessage = "The following characters appear more than once:\n"
        for letter, count in duplicates.items():
            violationMessage += f"{letter}: {count} times\n"
        violations.append(violationMessage)

    # Output - pass/fail
    if violations:
        print("Password validation failed due to the following:")
        for violation in violations:
            print(violation)
        return False
    else:
        print("Password is valid and OK to use.")
        return True


def main():
    # Prompt user for their full name
    userName = input("Enter full name such as John Smith: ")
    spaceIndex = userName.find(" ")  # Find the index of the space

    # Ensure a valid full name is entered
    if spaceIndex == -1:
        print("Please enter both a first and last name.")
        return

    # Extract first and last names
    firstName = userName[:spaceIndex].strip()
    lastName = userName[spaceIndex + 1:].strip()

    # Prompt for the new password
    password = input("Enter new password: ")

    # Validate password using the extracted names
    isValid = extractAndValidatePassword(firstName, lastName, password)
    
    if isValid:
        print(f"Welcome, {firstName} {lastName}!")

# Call the main function
main()