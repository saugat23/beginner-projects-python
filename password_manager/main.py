def add_password():
    password_for = input("What is this password for?: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(password_for + " - " + password + "\n")


def list_passwords():
   with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.strip())

def main():
    print("Hello from password-manager!")

    choice = int(input("Do you want to\n1. Add a password\n2. List a Password\n"))

    if choice == 1:
        add_password()
    elif choice == 2:
        list_passwords()
    else:
        print("Not a valid response!")

if __name__ == "__main__":
    main()
