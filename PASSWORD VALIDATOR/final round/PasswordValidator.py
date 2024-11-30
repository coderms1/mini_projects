# Password Validator Program

def validate_password(sPassword, sInitials):
    # Check length between 8 and 12 characters
    if len(sPassword) < 8 or len(sPassword) > 12:
        print("Password must be between 8 and 12 characters.")
        return False
    
    # Check that password does not start with 'Pass' or 'pass'
    if sPassword.startswith("Pass") or sPassword.startswith("pass"):
        print("Password can't start with Pass.")
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in sPassword):
        print("Password must contain at least 1 uppercase letter.")
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in sPassword):
        print("Password must contain at least 1 lowercase letter.")
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in sPassword):
        print("Password must contain at least 1 number.")
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^"
    if not any(char in special_characters for char in sPassword):
        print("Password must contain at least 1 of these special characters: ! @ # $ % ^")
        return False
    
    # Check that the password does not contain initials
    if sInitials.lower() in sPassword.lower():
        print(f"Password must not contain user initials: {sInitials}")
        return False
    
    # Check that no character appears more than once
    for char in set(sPassword):
        if sPassword.lower().count(char.lower()) > 1:
            print(f"These characters appear more than once: {char}")
            return False
    
    # If all conditions are satisfied
    print("Password is valid and OK to use.")
    return True


def main():
    # Prompt user for their first and last name
    sName = input("Enter your first and last name: ").strip()
    
    # Extract initials from the name
    first_name, last_name = sName.split()
    sInitials = first_name[0].upper() + last_name[0].upper()
    
    # Continue asking for a valid password until successful
    while True:
        sPassword = input("Enter your password: ").strip()
        
        if validate_password(sPassword, sInitials):
            break


if __name__ == "__main__":
    main()
