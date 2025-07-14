# Returns the middle char 
# of a string if its length is odd, 
# or the middle two chars if even.

def get_middle(s):
    if len(s) % 2 == 0:
        mid = len(s)//2
        return s[mid - 1 : mid + 1]
    else:
        mid = len(s)//2 
        return s[mid]
    

word = input("Enter word: ")
print(f"{get_middle(word)}")