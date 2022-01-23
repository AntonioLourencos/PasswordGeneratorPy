import os

if __name__ == "__main__":
    print("Installing packages")
    os.system("python3 -m pip install -r requirements.txt")
    print("Installed")
    while True:
        ask = input("Do you want to execute the password generator? (y/n): ")
        ask = ask.lower()
        if ask == "n":
            print("Ok, when you want to run generator read the instructions.")
            break
        elif ask == "y":
            os.system("python3 lib customParams")
            break

    print("Ok, closing...")
