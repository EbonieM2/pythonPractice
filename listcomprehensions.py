#Exercise 7 - List Comprehensions

'''
Write one line of Python that takes the list below and makes a new list that has
only the even elements of this list in it.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [num for num in a if num % 2 ==0]

print(even)
