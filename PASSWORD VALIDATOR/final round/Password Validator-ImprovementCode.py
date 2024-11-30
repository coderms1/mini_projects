def check_upper_lower_number(password):
    errors = []
    bUpper = False
    bLower = False
    bNumber = False
    #loop to check for conditions
    for char in password:
        if char.isupper():
            bUpper = True
        elif char.islower():
            bLower = True
        elif char.isdigit():
            bNumber = True
    #Appending error messages to a list
    if not bUpper:
        errors.append("Password must contain at least 1 uppercase letter")
    if not bLower:
        errors.append("Password must contain at least 1 lowercase letter")
    if not bNumber:
        errors.append("Password must contain at least 1 number 0-9")

    return errors