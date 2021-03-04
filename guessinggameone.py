#Exercise 9
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or
exactly right. (Hint: remember to use the user input lessons from the very first
exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print
this out.
'''
import random

num = random.randint(1,9)
guess = 0
count = 0

while guess != num and guess != "quit":
    guess = input("Guess a number between 1 and 9: ")

    if guess == "quit":
        break

    guess = int(guess)
    count += 1

    if guess > num:
        print("You guessed too high. Please guess again!")
    elif guess < num:
        print("You guessed too low. Please guess again!")
    else:
        print("Awesome! You guessed it in ", count, " tries!")
