'''
Ask the user for a number. Depending on whether the number is even or odd, print
out an appropriate message to the user. Hint: how does an even / odd number
react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number
to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.
'''

num = int(input("Please enter a number: "))

if num % 4 == 0:
    print(num, " is a multiple of 4!")
elif num % 2 == 0:
    print(num, " is an even number!")
else:
    print(num, " is an odd number!")


num2 = int(input("Please enter a number to check: "))
check = int(input("Please enter a number to divide by: "))

if num2 % check == 0:
    print(num2, " is a multiple of ", check, "!")
else:
    print(num2, " is not a multiple of ", check, "!")
