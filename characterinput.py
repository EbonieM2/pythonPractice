'''
Create a program that asks the user to enter their name and their age. Print out
a message addressed to them that tells them the year that they will turn 100
years old.

Extras:

Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message. (Hint: order of
operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
'''

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
