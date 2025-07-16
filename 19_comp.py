# Takes in 2 arrays (lists) and compares the first w/
# the second, checking against sqr root equivalencies 

def comp(array1, array2):
  if array1 is None or array2 is None:
    return False
  
  sq_list = [n ** 2 for n in array1] 
  if sorted(sq_list) == sorted(array2):
    return True

  return False

print(comp([1,2,3], [1,4,9]))