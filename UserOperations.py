from connect_mysql import connect_database

user_dict = {}

class UserOps:
    def __init__(self, library_id, birthdate):
        self.__id = library_id
        self.__birth_date = birthdate

    # define getters
    def get_id(self):
        return self.__id

    def get_birthdate(self):
        return self.__birth_date

def add_user(): 
    name = input("Enter the user's name: ") 
    library_id = input("Enter the user's library ID: ")
    birthdate = input("Enter the user's birthday: ")
    
    user_dict[name] = {
        "Library ID": library_id,
        "Birth Date": birthdate
    }

    print(f"{name} has been added to the list!")
    print(f"Contact: ", user_dict[name], sep="\n")

def view_user():
    name = input("Enter user's name: ")
    if name in user_dict:
        print(f"Contact: ", user_dict[name])
    else:
        print("There is no users in the system!")


def display_user():
    if user_dict:
        print("Your current contact list:", user_dict, sep="\n")
    else:
        print("No contacts in the current list")


def user_menu():
    while True:
        print("""
           *================*
            User Operations:
           *================* 
            1. Add a new user
            2. View user details
            3. Display all users
            4. Back to main menu
        """)

        book_menu = input("Enter a valid option: ")

        if book_menu == "1":
            add_user()
        elif book_menu == "2":
            view_user()
        elif book_menu == "3":
            display_user()
        elif book_menu == "4":
            break
        else:
            print("That's not a valid option, try again!")
    
user_menu()