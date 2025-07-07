#word_counter.py

#coder:sim
"""
This program takes your sentence and breaks it 
down to see how many times each word shows up. 
It doesn’t care about caps—just counts ‘em all up 
and shows you the list. Super helpful if 
you wanna see what words you use the most!
"""



entry = str(input("Write a sentence: "))

word_count = {}

words = entry.lower().split()

for word in words:
  if word in word_count:
    word_count[word] += 1
  else: 
    word_count[word] = 1

print("Here is a list of you word frequency: \n")

for word, count in word_count.items():
  print(f"{word}: {count}")