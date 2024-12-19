from connect_mysql import connect_database

# operations for books
book_dict = {}

conn = connect_database()
if conn is not None:
    cursor = conn.cursor()

class BookOps:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.availability = True

    # Getters
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_publication_date(self):
        return self.__publication_date
    
    def is_available(self):
        return self.availability

    # setters
    def set_availability(self, availability):
        self.availability = availability
    
    def display_info(self):
        status = "Available" if self.availability else "Borrowed"
        print(f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publication Date: {self.__publication_date}, Status: {status}")

# main functions
def add_book(): 
    title = input("Enter book title: ") 
    author = input("Enter book author: ") 
    genre = input("Enter book genre: ") 
    publication_date = input("Enter publication date: ")  
    
    # query to add book to the library
    query = "INSERT INTO books (title, author, genre, publication_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (title, author, genre, publication_date))
    conn.commit()
    query_display = "SELECT * FROM books WHERE title = %s"
    cursor.execute(query_display, (title, ))
    result = cursor.fetchall()
    
    print("Book has been added to the list!")
    print(f"Book:", result, sep="\n")

def borrow_book(): 
    title = input("Enter the title of the book you wish to borrow: ")
    query = "SELECT availability FROM books WHERE title = %s"
    cursor.execute(query, (title, ))
    result = cursor.fetchone()

    if result and result[0]:
        query = "UPDATE books SET availability = %s WHERE title = %s"
        cursor.execute(query, (False, title))
        conn.commit()
        print(f"Book '{title}' has been borrowed.")
    else: 
        print("This book is not available or does not exist in the database.")

def return_book():
    title = input("Enter the book you wish to return: ")
    query = "SELECT availability FROM books WHERE title = %s"
    cursor.execute(query, (title, ))
    result = cursor.fetchone()

    if not result[0]:
        query = "UPDATE books SET availability = %s WHERE title = %s"
        cursor.execute(query, (True, title))
        conn.commit()
        print(f"This {title} has been returned to the library")
    else:
        print("This book was not borrowed or does not exist in the database")

def search_book():
    title = input("Enter the book you wish to search for: ")
    
    # Query to search for books in the system
    query = "SELECT * FROM books WHERE title = %s"
    cursor.execute(query, (title, ))
    result = cursor.fetchall()
    print("Author results in database: ", result, sep='\n')
    
def display_book():
    # Query to display list of books in the database
    query = "SELECT * FROM books"
    cursor.execute(query)
    result = cursor.fetchall()
    print(" Books: ", result, sep="\n")

# Menu Control
def book_menu():
    while True:
        print("""
           *================*
            Book Operations:
           *================* 
            1. Add a new book
            2. Borrow a book
            3. Return a book
            4. Search for a book
            5. Display all books
            6. Back to main menu
        """)

        choice = input("Enter a valid option: ")

        if choice == "1": 
            add_book() 
        elif choice == "2": 
            borrow_book()
        elif choice == "3": 
            return_book()
        elif choice == "4":
            search_book() 
        elif choice == "5": 
            display_book() 
        elif choice == "6": 
            break 
        else: 
            print("Invalid option, please try again.")

if conn is not None: 
    try: 
        cursor = conn.cursor() 
        # Run the user menu 
        book_menu() 
         
    except Exception as e: 
        print(f"Error: {e}") 
    
    finally: 
        cursor.close() 
        conn.close() 
        print("Connection closed.")