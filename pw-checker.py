#pw-checker.py

# This is the first version of a BASIC Password Checker function that I wrote.
# May make some upgrades/updates to this script but planning to use something along
# these lines in my SAFU or NOT platform for new user sign-up. 

def pw_checker():

  sName = input("Enter first and last name: ")
  sFirst = sName.split()[0]
  sLast = sName.split()[1]
  sInitials = (sFirst[0] + sLast[0]).lower()

  while True:
    
    sPassword = input("Enter new password: ")

    bValid = True

    if len(sPassword) < 8 or len(sPassword) > 12:
      print("Password must be between 8 and 12 characters.")
      bValid = False
    
    if sPassword.lower().startswith("pass"):
      print("Password cannot start with 'PASS'.")
      bValid = False
    
    bUpper = False
    for char in sPassword:
      if char.isupper():
        bUpper = True
        break
    if not bUpper:
      print("Password must contain at least 1 uppercase character.")
      bValid = False

    bLower = False
    for char in sPassword:
      if char.islower():
        bLower = True
        break
    if not bLower:
      print("Password must contain at least 1 lowercase letter.")
      bValid = False
    
    bDigit = False
    for char in sPassword:
      if char.isdigit():
        bDigit = True
        break
    if not bDigit:
      print("Password must contain at least 1 number.")
      bValid = False

    sSpecials = "!@#$%^"
    bSpecial = False
    for char in sPassword:
      if char in sSpecials:
        bSpecial = True
        break
    if not bSpecial:
      print("Password must contain at least special character (!@#$%^).")
      bValid = False
    
    if sInitials in sPassword.lower():
      print("Password cannot contain user's initials.")
      bValid = False
    
    sChecked = ""
    bDuplicates = False
    for char in sPassword:
      if char not in sChecked:
        count = sPassword.lower().count(char)
        if count > 1:
          if not bDuplicates:
            print("The following characters appear more than once: ")
            bDuplicates = True
          print(f"{char}: {count} times")
          bValid = False
        sChecked += char
    
    if bValid:
      print("\nPassword has been accepted and is ready to use! ✅")
      break

pw_checker()

# ~ 🌛 MS1
