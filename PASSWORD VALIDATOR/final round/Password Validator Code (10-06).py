## Password Validator - Python 2 Coding Assignment (1)

## Author: Matthew Simone
## Date: 09/24/2024
## Instructor: Professor Candido


# 1. Prompt the user for their First and Last name and store the input into a variable called sName.

sName = string(input("Please enter your first and last name: "))
sPassword

# 2. Code a loop that will keep asking for a password UNTIL a valid password in entered.



#3. Prompt the user for their desired password and store their response in a variable called sPassword.


#4. Extract out the first initial from the first name and the first initial of the last name from the variable sName
# and put in a new variable called sInitials. For example if Brian Candido is in the sName variable then the
# sInitials should contain BC. You can assume the user will enter 1 first name and 1 last name.

#5. Check to make sure the sPassword length is between 8 and 12 characters. If the password is not within
# the required length write out the message: Password must be between 8 and 12 characters.

#6. Check to make sure the sPassword starts does not start with Pass or pass. If not write out the Password
# can’t start with Pass.

#7. Check to make sure the sPassword contains at least 1 uppercase letter A through Z. If not write out the
# message: Password must contain at least 1 uppercase letter.

#8. Check to make sure the sPassword contains at least 1 lowercase letter a through z. If not write out the
# message: Password must contain at least 1 lowercase letter.

#9. Check to make sure the sPassword contains at least 1 number between 0 and 9. If not write out the
# message: Password must contain at least 1 number.

#10. Check to make sure the sPassword contains at least 1 of these special characters: ! @ # $ % ^. If not write
# out the message: Password must contain at least 1 of these special characters: ! @ # $ % ^

#11. Check to make sure the sPassword does not contain the value of sInitials within the string. For example
# sPassword cannot contain BC or bc or any variation of BC so you will need to convert to either lowercase
# or uppercase than compare using Python string functions. If not write out the message: Password must not
# contain user initials.

#12. No character can be present more than once. Write code to process each character in the password and keep
# track of how many occurrences are present. If any character (either uppercase or lowercase versions) is in
# the password more than 1 output the character and how many occurrences and print out the message: These
# characters appear more than once:
    
#13. If sPassword passes all the above checks output this message: Password is valid and OK to use. And exit
# the loop.

#14. Make sure your code has a main() function. It is your optional choice if you want additional functions. 
