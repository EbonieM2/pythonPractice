current_year = 2021
tgt_age = 100
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

diff = tgt_age - age
year100 = current_year + diff
msg100 = "Congratulations! You are already 100 years old!"

if age < 100:
    print(name + ", you will be 100 years old in the year " + str(year100) + "!")
else:
    print("Congratulations! You are already 100 years old!")

new_num = int(input("Please enter a number between 1 and 20: "))

print("Congratulations! You are already 100 years old!\n"*new_num)
