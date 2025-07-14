# Returns a string in the format "errors/total" 
# where errors are the count of chars in the input 
# string that are greater  than 'm', and total is the string length.

def printer_error(s):
    err = 0
    count = 0
    for char in s:
        if char > 'm':
            err += 1
            count += 1
        else:
            count += 1
    return f"{err}/{count}"

string = input("enter: ")
print(f"{printer_error(string)}")