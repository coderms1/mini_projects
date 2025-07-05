# 02_decorators.py

# Decorators are a way to modify or enhance functions or methods in Python.

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{str(end - start)} seconds to run")
    return wrapper 

print()

@timer
def sum_to_one_milly():
    total = 0
    for i in range(10_000_000):
        total += i
    print(total)

sum_to_one_milly()

def my_decorator(func):
    def wrapper():
        print(f"Now running: {func.__name__} function")
        func()
    return wrapper

@my_decorator
def say_whatsup():
    print("What's up!?")

say_whatsup()
