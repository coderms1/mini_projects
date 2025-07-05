#03_list_comprehension.py

# List comprehensions are a concise way to create lists in Python.

sq_nums1 = []

for i in range(1, 11):
    sq_nums1.append(i*i)

print(sq_nums1)

# BETTER WAY TO DO IT 👇

# Using a list comprehension
sq_nums2 = [i*i for i in range(1, 11)]
print(sq_nums2)

# Using a dictionary comprehension
sq_nums3 = {i : i*i for i in range(1, 11)}
print(sq_nums3)

# Using a condition in a comprehensive list
even_squares = [i*i for i in range(1, 11) if i % 2 == 0]
print(even_squares)


def timer(func):
    def wrapper():
        import time
        start = time.time()
        func()
        end = time.time()
        print(f"{str(end - start)} seconds to run")
    return wrapper

# list comprehension vs for loop (performance comparison)

@timer
def for_loop_example():
    for i in range(1_000_000):
        result = []
        for i in range(1, 11):
            result.append(i * i)

@timer
def list_comprehension_example():
    for _ in range(1_000_000):
        result = [i * i for i in range(1, 11)]

print("For loop: ")
for_loop_example()
print("- "* 5)
print("List comprehension:")
list_comprehension_example()    

