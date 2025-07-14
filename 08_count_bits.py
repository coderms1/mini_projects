# Converts an int to binary and returns the count 
# of '1' bits in its binary representation. 

def count_bits(n):
    n = bin(n) 
    count = 0
    for char in n: 
        if char == '1':
            count += 1
        
    return count

print(f"{count_bits(1234)}")