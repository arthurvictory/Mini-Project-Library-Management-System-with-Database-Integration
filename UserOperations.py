from connect_mysql import connect_database

user_dict = {}

conn = connect_database()
if conn is not None:
    cursor = conn.cursor()

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
    
    # query to add User to database    
    query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
    cursor.execute(query, (name, library_id))
    conn.commit()
    query_display = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query_display, (name, ))
    result = cursor.fetchall()

    print(f"User:", result, sep="\n")

def view_user():
    name = input("Enter user's name: ")

    # query to view a user in the database
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (name, ))
    result = cursor.fetchall()
    print("User result in database: ", result, sep='\n')


def display_user():
    # query to display all users in the database
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    print("Users: ", result, sep="\n")


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