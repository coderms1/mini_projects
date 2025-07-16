# Formats a list of 10 digits into a phone number 
# string to meet the format: (xxx) xxx-xxxx.

def create_phone_number(n):
  first = n[0:3]
  mid = n[3:6]
  last = n[6:10]
  
  f = ''.join(str(d) for d in first)
  m = ''.join(str(d) for d in mid)
  l = ''.join(str(d) for d in last)

  return f"({f}) {m}-{l}"

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))