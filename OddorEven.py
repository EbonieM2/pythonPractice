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
