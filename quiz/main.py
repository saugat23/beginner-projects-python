def main():
    print("Hello from quiz!")
    points = 0

    decision = str(input("Do you want to play? \n"))
    if(decision=="no") :
        print("Fair Enough, bye!!")
        quit()
    elif(decision=="yes"):
        answer = input("What does a CPU stand for? ").lower().replace(" ", "")
        if(answer=="centralprocessingunit"):
            print("That's correct, 1 point added!!")
            points = points + 1
        else:
            print("Wrong, no points added.")
        answer2 = input("What is the PH value of water? ")
        if(int(answer2) == 7):
            print("That's correct, 1 point added!!")
            points = points + 1
        else:
            print("Wrong, no points added.")
        answer3 = input("How many colors are there in the rainbows? ")
        if(int(answer3) == 7):
            print("That's correct, 1 point added!!")
            points = points + 1
        else:
            print("Wrong, no points added!!")

        print(f"\n\nWe are at the end of the quiz. Thanks for playing.\nYour score is {points}/3.")
    else:
        print("Invalid response, Response should either be yes or no. Aborting!")
        quit()

if __name__ == "__main__":
    main()
