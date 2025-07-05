# 01_generators.py

# Generators are a way to create iterators in Python using a function that yields values one at a time.

def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

for number in count_up_to(5):
    print(number)
