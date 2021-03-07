# Exercise 20 - Element Search

'''
Write a function that takes an ordered list of numbers (a list where the elements
are in order from smallest to largest) and another number. The function decides
whether or not the given number is inside the list and returns (then prints) an
appropriate boolean.

Extras:

Use binary search.
'''
import random


def find(ordered_list, number):
    for n in list:
        if n == number:
            return True
    return False

list = random.sample(range(0, 85), 20)
print(list)

print(find(list, 16))
print(find(list, 25))
print(find(list, 60))
print(find(list, 2))
print(find(list, 84))
