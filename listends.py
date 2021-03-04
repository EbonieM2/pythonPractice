#Exercise 12 - List Ends
'''
Write a program that takes a list of numbers and makes a new list of only the
first and last elements of the given list. For practice, write this code inside
a function.
'''

a = [5, 10, 15, 20, 25]

#
# def list_ends(a):
#     return[a[0], a[len(a)-1]]

def list(a):
    return [a[0], a[-1]]

print(list(a))
