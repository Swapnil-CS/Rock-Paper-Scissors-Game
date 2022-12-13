from random import randint

print("\t\t****** Welcome to Rock Paper Scissors Game ******")

choice = ["rock", "paper", "scissors"]

round = int(input("\n\tHow many round do you want in the game? "))

r = round
pcnt = 0
ccnt = 0

while round > 0:

    computer = choice[randint(0, 2)]

    player = input('''\n\tWhat's your choice?
    \t\t[rock, paper, scissors]? ''')

    if player == computer:
        print("\n\tIts a Tie round! Both You and Computer chose", player)

        round -= 1

    elif player == "rock":
        if computer == "paper":
            ccnt += 1
            print("\n\tYou Lose the round! Computer's",
                  computer, "covers Your", player)
        else:
            pcnt += 1
            print("\n\tYou Win the round! Your", player,
                  "smashes Computer's", computer)

        round -= 1

    elif player == "paper":
        if computer == "rock":
            pcnt += 1
            print("\n\tYou Win the round! Your",
                  player, "covers Computer's", computer)
        else:
            ccnt += 1
            print("\n\tYou Lose the round! Computer's",
                  computer, "cut your", player)

        round -= 1

    elif player == "scissors":
        if computer == "rock":
            ccnt += 1
            print("\n\tYou Lose the round! Computer's",
                  computer, "smashes Your", player)
        else:
            pcnt += 1
            print("\n\tYou Win the round! Your",
                  player, "cut Computer's", computer)

        round -= 1

    else:
        print("\n\tThat's not a valid choice! Please enter a valid choice")

    print("\n\tScore at the end of Round -", r - round)
    print("\tYou:", pcnt, "\tComputer:", ccnt)

if pcnt > ccnt:
    print("\n\t\t*** Congratulations! You WON the game ***")

elif pcnt < ccnt:
    print("\n\t\t*** Oops! You LOST the game. Better luck next time ***")

else:
    print("\n\t\t*** Wow! The game is TIED ***")

print("\n\t\t****** Final Score ******")
print("\t\tYou:", pcnt, "\tComputer:", ccnt)
print("\n\t\tThanks for playing the game :)")
