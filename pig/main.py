import random


def evaluate_result(user1, user2):
    if user1 > user2:
        print(f"User 1 won by {user1 - user2} points!")
    else:
        print(f"User 2 won by {user2 - user1} poinst!")

def main():
    print("Hello from pig!")

    MAX_SCORE=50
    USER1_SCORE=0
    USER2_SCORE=0

    user1_choice = input("User 1's turn! Are you ready? (y/n): ")
    if user1_choice == "y":
        while USER1_SCORE < MAX_SCORE:
            play1_choice = input("Do you want to roll a dice or quit? (r/q): ")
            match (play1_choice) :
                case "r":
                    score = random.randint(2,6)
                    print(f"You scored a {score}")
                    if score == 1:
                       USER1_SCORE = 0
                       print(f"User 1's total score is {USER1_SCORE}")
                       break
                    else:
                        USER1_SCORE += score
                case "q":
                    print(f"User1's score is {USER1_SCORE}")
                    break
                case _:
                    print("Invalid command!")
                    break

        if(USER1_SCORE >= MAX_SCORE):
            print("User 1 won!! Score reached 50.")
            return

    else:
        print("Alright, no sufficient players, game is ending!")
        return

    user2_choice = input("User 2's turn! Are you ready? (y/n): ")
    if user2_choice == "y":
        while USER2_SCORE < MAX_SCORE:
            play2_choice = input("Do you want to roll a dice or quit? (r/q): ")
            match (play2_choice) :
                case "r":
                    score = random.randint(2,6)
                    print(f"You scored a {score}")
                    if score == 1:
                       USER2_SCORE = 0
                       print(f"User 1's total score is {USER1_SCORE}")
                       break
                    else:
                        USER2_SCORE += score
                case "q":
                    print(f"User2's score is {USER2_SCORE}")
                    break
                case _:
                    print("Invalid command!")
                    break

        if(USER2_SCORE >= MAX_SCORE):
            print("User 2 won!! Score reached 50.")
            return

    else:
        print("Alright, no sufficient players, game is ending!")
        return

    evaluate_result(USER1_SCORE, USER2_SCORE)

if __name__ == "__main__":
    main()
