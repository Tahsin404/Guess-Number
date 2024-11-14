import random

num_gen = random.randint(1, 100)
integer = num_gen


def num(attempts):
    while attempts > 0:
        print("Guess the Number \n")

        try:
            player_guess = int(input("Type a number!\n"))
            print("*" * 30)
            if 1 <= player_guess <= 100:
                if attempts == 1 and player_guess is not integer:
                    print("Game Over You Have Used All Your Attempts")
                    return f"You guessed {player_guess} while it was actually {integer}"

                elif player_guess < integer:
                    print("Good Guess but guess higher!\n")
                    print("*" * 30)
                elif player_guess > integer:
                    print("Good guess but guess lower\n")
                    print("*" * 30)
                else:
                    return "Great Guess! You are correct!"
                attempts -= 1
            else:
                print("Please Choose a number between 1 and 100\n")

        except ValueError:
            print("Invalid input, Please input an integer between 1 and 100")


while True:
    try:
        player_attempts = int(input("How Many attempts would you like?"))
        if player_attempts > 10:
            print("Please Choose less than 10 Attempts")
        elif player_attempts > 0:
            break
        else:
            print("Please Choose a positive integer between 1 and 10")
    except ValueError:
        print("Invalid input. Attempts should be a positive integer between 1 and 10")


print(num(player_attempts))
