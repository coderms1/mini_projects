#06_dunders.py 

# Dunders and Class Methods 
# Dunder = Double Underscore Methods 


## 001: Using __init__ dunder method:
# class Rectangle:
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y

# Rectangle(2, 3)


# # 002: __add__ & __len__ dunder methods:
# str1 = "hello"
# str2 = "dudes"

# new_str = str1.__add__(str2)
# len_str = str1.__len__()

# print(new_str) 
# print(len_str)


# # 003: - Create Counter class with dunder methods
# class Counter:
#     def __init__(self):
#         self.value = 1

#     def count_up(self):
#         self.value += 1

#     def count_down(self):
#         self.value -= 1

#     def __str__(self):
#         return f"Counter: {self.value}"
    
#     def __add__(self, other):  # self = count1 || other = count2
#         if isinstance(other, Counter):
#             return self.value + other.value
#         raise Exception("Invalid - must be Counter type.")

# count1 = Counter()
# count2 = Counter()

# count1.count_up()
# count2.count_up()

# print(count1, count2)
# print(count1 + count2) 

# # 004: Create a class with __str__ and __repr__ dunder methods

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # __str__ is for output 
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    # __repr__ is a debugging dunder method
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"
    
# Instance of the Car class
car1 = Car("Ford", "Mustang", 2008)

# Print out the object using __str__ dunder method
print(str(car1)) # Output -> for user
print(repr(car1)) # Output -> for debugging