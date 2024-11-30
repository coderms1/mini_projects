# Assignment: Password Validator
# Class: CIT-117 ~ (Python-2 w Prof C)
# Author: Matthew Simone
# Due Date: 10/06/24

def validatePassword(userPassword, userInitials):
    """
    This function performs validation checks on the password and
    collects error messages if any rules are violated, including repeated characters.
    """
    # Initialize necessary variables for password characteristics
    specialChars = "!@#$%^"
    charCount = {}
    hasUpperChar = False
    hasLowerChar = False
    hasDigitChar = False
    hasSpecialChar = False

    # Analyze password characteristics in a loop
    for letter in userPassword:
        lowerLetter = letter.lower()
        charCount[lowerLetter] = charCount.get(lowerLetter, 0) + 1
        
        if letter.isupper():
            hasUpperChar = True
        if letter.islower():
            hasLowerChar = True
        if letter.isdigit():
            hasDigitChar = True
        if letter in specialChars:
            hasSpecialChar = True

    # Define validation rules and conditions in a dictionary
    ruleChecks = {
        "Password must be between 8 and 12 characters.": (8 <= len(userPassword) <= 12),
        "Password can't start with 'Pass'.": not (userPassword.lower().startswith("pass")),
        "Password must contain at least 1 uppercase letter.": hasUpperChar,
        "Password must contain at least 1 lowercase letter.": hasLowerChar,
        "Password must contain at least 1 number.": hasDigitChar,
        "Password must contain at least 1 special character (!@#$%^).": hasSpecialChar,
        "Password must not contain user initials.": userInitials.lower() not in userPassword.lower(),
    }

    # List to collect any brokenRules
    brokenRules = []

    # Check all validation conditions
    for message, condition in ruleChecks.items():
        if not condition:
            brokenRules.append(message)

    # Check for repeated characters
    duplicates = {letter: count for letter, count in charCount.items() if count > 1}
    if duplicates:
        errorMessage = "The following characters appear more than once:\n"
        for letter, count in duplicates.items():
            errorMessage += f"{letter}: {count} times\n"
        brokenRules.append(errorMessage)

    # Display results based on brokenRules
    if brokenRules:
        print("Password validation failed due to the following:")
        for violation in brokenRules:
            print(f"- {violation}")
        return False
    else:
        print("Password is valid and OK to use.")
        return True

# Find index of space
def extractNames(userName):
    """
    This function manually extracts the first and last name from the user's input using indexing and a loop.
    """
    spaceIndex = userName.find(" ")  
    firstName, lastName = "", ""

    
    for charIndex in range(len(userName)):
        if charIndex == 0:  
            firstName += userName[charIndex].upper()
        elif charIndex < spaceIndex:
            firstName += userName[charIndex].lower()
        elif charIndex > spaceIndex and userName[charIndex] != " ":
            lastName += userName[charIndex].lower()

    return firstName, lastName

def main():
    """
    The main function handles user input and orchestrates the password validation process.
    """
    
    # Step 1: Prompt user for first and last name
    userName = input("Enter your first and last name: ")
    
    # Step 4: Extract initials from the first and last name using the manual method
    firstName, lastName = extractNames(userName)
    
    # Ensure first and last name have been entered
    if not firstName or not lastName:
        print("Please enter both a first and last name.")
        return
    
    userInitials = firstName[0].upper() + lastName[0].upper()  # Combine first initials from both names
    
    # Step 2: Loop until a valid password is entered or user chooses to exit
    while True:
        # Step 3: Prompt for the desired password
        userPassword = input("Enter new password (or press Enter to exit): ")
        
        # Exit if the user presses Enter without entering a password
        if userPassword == "":
            break
        
        # Call the validatePassword function to perform all checks
        if validatePassword(userPassword, userInitials):
            # Step 13: Exit loop if password is valid
            break


# Call the main function directly
main()