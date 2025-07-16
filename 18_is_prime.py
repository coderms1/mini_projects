# Takes in a number and spits back out a print statement 
# (True or False) as to whether it is a prime number or not.

def is_prime(num):
  if num <= 1: 
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
      
  return True
  
print(is_prime(1))