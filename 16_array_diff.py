# Returns elements in list a that are 
# not in list b. 

def array_diff(a, b):
    dif = []
    for i in a:
        if i not in b:
            dif.append(i)
    return dif

a = [1,2,1,2,4]
b = [1,2]

print(array_diff(a, b))