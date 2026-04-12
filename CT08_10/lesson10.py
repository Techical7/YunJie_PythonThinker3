# Task 1
import random

def generate_password(length):
    
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    all_charaters = uppercase + lowercase + digits + special
    
    password_charaters = [
        random.choice(uppercase + lowercase + digits + special)
        ]
    for _ in range(length):
        password_charaters.append(random.choice(all_charaters))
    random.shuffle(password_charaters)
    return ''.join(password_charaters)

if __name__ == "__main__":
    password = generate_password(12)
    print(f"Generated password: {password}")

# Task 2
import string

def create_new_user(user_db, username=None, password_length=16):

    if username is None:
        username = f"user{len(user_db)}"
    if username in user_db:
        raise KeyError(f"Username '{username}' already exists.")

    user_db[username] = password
    print(f"Username: {username}")
    print(f"Password: {password}")
    return user_db

if __name__ == "__main__":
    users = {}
    create_new_user(users)

# Task 3
def update_password(user_db):
    username = input("Enter your username: ")
    if username not in user_db:
        print("Username not found.")
        return user_db

    current_password = input("Enter your current password: ")
    if user_db[username] != current_password:
        print("Incorrect current password.")
        return user_db

    new_password = generate_password()
    user_db[username] = new_password
    print(f"Username: {username}")
    print(f"New Password: {new_password}")
    return user_db

# ## Task 4: Login

# ## Allows users to log in by verifying their username and password.

# - **Function name**: `login()`

# - **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.

# - **returns**: auth_status(boolean) – True or False indicating success or failure.

# ### Notes
# *Ensures the username exists in user_db.*

# *Matches the entered password with the stored password for validation.*

# ## Task 5: View Username and passwords
# ### Displays all stored usernames and their masked passwords (e.g., ********)

# - **Function name**: `view_user_data()`

# - **Params**: user_db (dictionary) – A dictionary to store usernames and passwords.

# - **returns**: none
#   - Prints a list of username and passwords

# ### Notes
# *Strictly speaking, this function should not exist in any system, as it could lead to abuse of a user’s private data.*

# *But for verifying whether your program works, we have put this in.*

# *Challenge: Mask part of the password. i.e. put (*) instead of the real password.*

# ## Task 6: Build a menu system

# ### Build a menu that allows you to access all the functions in the system.

# - **Function name**: view_menu()

# - **Params**: none

# - **returns**: none

# ### Notes
# *The following menu options should be available to you.*

# *Your menu should validate the available options inputted by the user.*