import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user_data = {}

def register():
    username = input("Enter a new username: ")
    if username in user_data:
        print("Username already exists! Try a different one.")
        return
    
    password = input("Enter a new password: ")
    hashed_pw = hash_password(password)
    user_data[username] = hashed_pw
    print(f"User {username} registered successfully!")

def login():
    username = input("Enter your username: ")
    if username not in user_data:
        print("Username does not exist!")
        return False
    
    password = input("Enter your password: ")
    hashed_pw = hash_password(password)
    print(hashed_pw)
    if user_data[username] == hashed_pw:
        print(f"User {username} logged in successfully!")
        return True
    else:
        print("Invalid password!")
        return False


def change_password():
    username = input("Enter your username: ")
    if username not in user_data:
        print("Username does not exist!")
        return
    
    old_password = input("Enter your current password: ")
    if user_data[username] != hash_password(old_password):
        print("Incorrect current password!")
        return
    
    new_password = input("Enter your new password: ")
    user_data[username] = hash_password(new_password)
    print("Password updated successfully!")


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Change Password\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                print("You are now logged in!")
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

main()