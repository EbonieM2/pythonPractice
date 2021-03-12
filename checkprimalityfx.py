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
