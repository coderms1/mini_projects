# Calculates the number of times 
# you must multiply the digits of 
# a number together until a single-digit number 
# is obtained.

def persistence(n):
    step = 0
    while n >= 10:
        new = 1
        for num in str(n):
            new *= int(num)
        n = new    
        step += 1
    return step