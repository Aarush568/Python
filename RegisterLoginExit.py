usernames = []
passwords = []
def register():
    username = input("Enter username: ")
    if username in usernames:
        print("Username already exists! Try another one.")
        return
    password = input("Enter password: ")
    usernames.append(username)
    passwords.append(password)
    print("User registered successfully!")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in usernames:
        index = usernames.index(username)
        if passwords[index] == password:
            print("Login Successful!")
        else:
            print("Incorrect password!")
    else:
        print("Username not found!")
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select option: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")
main()