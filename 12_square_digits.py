# Squares each digit of an input number and 
# concatenates the results into a single int.
def square_digits(num):
    ret = ''
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

print(f"{square_digits(9119)}")