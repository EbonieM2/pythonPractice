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
