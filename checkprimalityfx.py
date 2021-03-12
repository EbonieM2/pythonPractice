'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
'''


#exercise 4 solution:

num = int(input("Please enter a number: "))
y = [n for n in range(2, num) if num % n == 0]

def isprime(n):
    if num > 1:
        if len(y) == 0:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
    else:
        print(num, "is not a prime number")

isprime(num)


#List Comprehension Sample solution

# Assumes that "a" contains an integer > 2 whose primality needs to be verified
# The algorithm builds a list of factors including the number 2 and all odd numbers
# up to the square root of "a", and then checks if any of those numbers divides "a"
# without a remainder - if so then "a" is not prime, else it is

# if sum([ True if a%factor == 0 else False for factor in ( [2] + list(range(3,int(math.sqrt(a))+1,2) )) ]):
#   print("Number is composite")
# else:
#   print("Number is prime")
