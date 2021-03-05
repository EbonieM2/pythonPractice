# Exercise 13 - Fibonacci

'''
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can use
functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers
in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def fibonacci():
    num = int(input("How many numbers in the sequence do you want to generate?: "))
    n = 1

    if num == 0:
        fib_seq = []
    elif num == 1:
        fib_seq = [1]
    elif num == 2:
        fib_seq = [1,1]
    elif num > 2:
        fib_seq = [1,1]
        while n <(num - 1):
            fib_seq.append(fib_seq[n] + fib_seq[n-1])
            n += 1
    return fib_seq

print(fibonacci())
input()
