num = int(input("Please enter a number: "))

if num % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")

if num % 4 == 0:
    print("This number is also a multiple of 4!")

num2 = int(input("Please enter a new number: "))
check = int(input("Please enter a check number: "))

if num2 % check == 0:
    print("Num2 is a multiple of check!")
else:
    print("Num2 cannot be evenly divided by check!")
