# Exercise 28 - Max of Three

'''
Implement a function that takes as input three variables, and returns the largest
of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally
takes care of for us. All you need is some variables and if statements!
'''



def maxofthree(x,y,z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)

maxofthree(25,7,89)
