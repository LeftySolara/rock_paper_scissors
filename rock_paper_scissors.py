from random import choice


def play_round(options, outcomes, player_score, com_score):
    """ Returns true if player wins, false if loss, or none if tie """
    p_choice = input("Choose rock, paper, or scissors: ")
    while p_choice not in options:
        p_choice = input("Invalid option. Try again: ")

    c_choice = choice(options)
    result = (p_choice, c_choice)

    print("Your choice: {}\nComputer's choice: {}".format(p_choice, c_choice))

    if result == outcomes[0] or result == outcomes[4] or result == outcomes[8]:
        print("It's a tie!")
        return None
    elif result == outcomes[2] or result == outcomes[3] or result == outcomes[7]:
        print("You win!")
        return True
    elif result == outcomes[1] or result == outcomes[5] or result == outcomes[6]:
        print("You lost!")
        return False
    else:
        print("Error!")

    print("Current score:")
    print("You: {}, Computer: {}".format(player_score, com_score))


def main():
    options =  ["rock", "paper", "scissors"]
    outcomes = [("rock",    "rock"), ("rock",    "paper"), ("rock",    "scissors"),
                ("paper",   "rock"), ("paper",   "paper"), ("paper",   "scissors"),
                ("scissors","rock"), ("scissors","paper"), ("scissors","scissors")
                ]
    
    player_score = 0
    com_score = 0
    cont = 'Y'

    print("Rock Paper Scissors")
    print()

    while cont.upper() == 'Y':
        result = play_round(options, outcomes, player_score, com_score)

        if result == None:
            pass
        elif result:
            player_score += 1
        elif not result:
            com_score += 1

        print("Current scores:")
        print("You: {}\nComputer: {}".format(player_score, com_score))
        print()

        cont = input("Play again(Y/N)? ")
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()