from connect_mysql import connect_database

author_dict = {}

conn = connect_database()
if conn is not None:
    cursor = conn.cursor() 

class AuthorOps:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
    
    # set getters
    def get_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography
    
def add_author():
    name = input("Enter the Author's name: ") 
    biography = input("Enter the Author's Biography: ")

    # query to add Author to database    
    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, biography))
    conn.commit()
    query_display = "SELECT * FROM authors WHERE name = %s"
    cursor.execute(query_display)
    result = cursor.fetchall()
    
    print("Author has been added to the list!")
    print(f"Author:", result, sep="\n")

def view_author():
    name = input("Enter Author's name: ")
    # query to view the a specific Author in the database
    query = "SELECT * FROM authors WHERE name = %s"
    cursor.execute(query, (name))
    result = cursor.fetchall()
    print("Author results in database: ", result, sep='\n')

def display_authors():
    # Query to display list of Authors in the database
    query = "SELECT * FROM authors"
    cursor.execute(query)
    result = cursor.fetchall()
    print(" Authors: ", result, sep="\n")

def user_menu():
    while True:
        print("""
           *================*
            User Operations:
           *================* 
            1. Add a new Author
            2. View author details
            3. Display all authors
            4. Back to main menu
        """)

        book_menu = input("Enter a valid option: ")

        if book_menu == "1":
            add_author()
        elif book_menu == "2":
            view_author()
        elif book_menu == "3":
            display_authors()
        elif book_menu == "4":
            break
        else:
            print("That's not a valid option, try again!")