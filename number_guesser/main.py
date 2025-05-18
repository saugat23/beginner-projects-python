import random


def main():
    print("Hello from number-guesser!")
    number = random.randint(1, 100)

    guess = int(input("Enter your guess between 1 to 100: "))
    while(guess!=number):
        if(guess < number):
            print("Number is higher.")
            new_guess = int(input("Guess Again: "))
            guess=new_guess
        elif(guess > number):
            print("Number is lower.")
            new_guess=int(input("Guess Again: "))
            guess=new_guess

    print(f"Yes, you found the number, it was {number}")
if __name__ == "__main__":
    main()
