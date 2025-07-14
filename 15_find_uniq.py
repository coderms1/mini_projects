# Finds and returns the unique number in an
# array where all other numbers are the same.

def find_uniq(arr):
    if arr[0] == arr[1]:
      common = arr[0]
    else:
      common = arr[2]
      
    for n in arr:
      if n != common:
        return n   # n: unique number in the array

arr = [1, 1, 2, 1, 1, 1, 1, 1]
print(find_uniq(arr))