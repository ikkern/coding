import random


def guess_the_number():
    """Function to let the user guess a randomly generated number between 1 and 10."""
    random_number = random.randint(1, 10)

    while True:
        try:
            guess = input("Guess the number (1-10): ").strip()

            if not guess.isdigit():
                print("Invalid input! Please enter a number between 1 and 10.")
                continue

            guess = int(guess)

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess == random_number:
                print("Correct! 🎉")
                break
            else:
                print("Wrong, try again!")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 10.")


if __name__ == "__main__":
    guess_the_number()
