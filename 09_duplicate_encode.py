# Converts a string to a new string where each character 
# is '(' if it appears once in the input (case-insensitive), 
# or ')' if it appears multiple times.

def duplicate_encode(word):
    ret = ""
    word = word.lower()
    for char in word:
        if word.count(char) == 1:
            ret += "("
        else:
            ret += ")"
            
    return ret
      
input = input("Enter word: ")
print(f"{duplicate_encode(input)}")