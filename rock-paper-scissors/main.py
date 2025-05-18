import random


def main():
    print("Hello from rock-paper-scissors!")

    user_wins = 0
    computer_wins = 0
    guess_list = ["rock", "paper", "scissors"]

    while user_wins != 5 and computer_wins != 5:
        computer_choice = random.choice(guess_list)
        user_choice = input("Choose Rock, Paper or Scissors: ")

        if (user_choice.lower() == "rock" and computer_choice == "scissors") or \
           (user_choice.lower() == "scissors" and computer_choice == "paper") or \
           (user_choice.lower() == "paper" and computer_choice == "rock"):
            print(f"Computer chose : {computer_choice}")
            print("You win! Point added!!")
            user_wins += 1
        elif (user_choice.lower() == "rock" and computer_choice == "paper") or \
             (user_choice.lower() == "scissors" and computer_choice == "rock") or \
             (user_choice.lower() == "paper" and computer_choice == "scissors"):
            print(f"Computer Chose : {computer_choice}")
            print("Computer Won, points added!!")
            computer_wins += 1
        elif user_choice.lower() == computer_choice:
            print(f"Computer Chose : {computer_choice}")
            print("It's a draw, no points added!")
        else:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")

    print(f"The score is \n \t User - {user_wins} \n \t Computer - {computer_wins}")

if __name__ == "__main__":
    main()
