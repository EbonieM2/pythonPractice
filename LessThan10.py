'''Take a list and write a program that prints out all the elements of the list
that are less than 5.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = []

for n in a:
    if n < 5:
        print(n)

print('*'*50)

'''
Extras:
Instead of printing the elements one by one, make a new list that has all the
elements less than 5 from this list in it and print out this new list.'''

for n in a:
    if n < 5:
        x.append(n)
print(x)

'''Write this in one line of Python.'''
print([n for n in a if n<5])

'''
Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.
'''
x2 = []

num = int(input("Please enter a number: "))

for n in a:
    if n < num:
        x2.append(n)
print(x2)
