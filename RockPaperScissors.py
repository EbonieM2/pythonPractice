'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

player1 = input("Player 1 please enter rock, paper or scissors: ").casefold()
player2 = input("Player 2 please enter rock, paper or scissors: ").casefold()

while (player1 == 'rock') and (player2 == 'scissors'):
    print("Player1 wins; Rock beats Scissors")
    break
if (player1 == 'rock') and (player2 == "paper"):
    print("Player2 wins; Paper covers Rock")
elif (player1 == 'rock') and (player2 == 'rock'):
    print("It's a draw. You both played Rock.")

while (player1 == 'paper') and (player2 == 'scissors'):
    print("Player2 wins; Scissors cuts Paper")
    break
if (player1 == 'paper') and (player2 == "rock"):
    print("Player1 wins; Paper covers Rock")
elif (player1 == 'paper') and (player2 == 'paper'):
    print("It's a draw. You both played Paper.")

while (player1 == 'scissors') and (player2 == 'rock'):
    print("Player2 wins; Rock smashes Scissors")
    break
if (player1 == 'scissors') and (player2 == "paper"):
    print("Player1 wins; Scissors cut Paper")
elif (player1 == 'scissors') and (player2 == 'scissors'):
    print("It's a draw. You both played Scissors.")


'''
Sample Solution:

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
'''
