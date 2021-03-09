# Exercise 14: List Remove Duplicates

'''
Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a
list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a
different function.
'''

nlist = [1, 3, 3, 4, 6, 7, 7, 8, 6, 9, 10, 11, 11, 13, 16, 17, 17, 26, 35, 35]

def numlist(list):
    list = set(list)
    print(list)

numlist(nlist)


# def dedup(list):
#     gl = []
#     for n in list:
#         if n not in gl:
#             gl.append(n)
#     return gl
#     print(gl)
# dedup(nlist)
