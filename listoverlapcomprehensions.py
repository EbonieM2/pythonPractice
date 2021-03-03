#Exercise 10 - List Overlap comprehensions
import random

'''
Take two lists and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes. Write this in one line of Python
using at least one list comprehension. (Hint: Remember list comprehensions from
Exercise 7).
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [num for num in b if num in a]
print(c)


rl1 = random.sample(range(0, 45), 15)
print(sorted(rl1))

rl2 = random.sample(range(5, 30), 8)
print(sorted(rl2))

rl3 = [num for num in rl2 if num in rl1]
print(rl3)


# even = [num for num in a if num % 2 ==0]
