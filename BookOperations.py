from connect_mysql import connect_database

# operations for books
book_dict = {}

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
    book = BookOps(title, author, genre, publication_date) 
    book_dict[title] = book 
    print(f"Book '{title}' added successfully!")

def borrow_book(): 
    title = input("Enter the title of the book you wish to borrow: ") 
    if title in book_dict and book_dict[title].is_available(): 
        book_dict[title].set_availability(False)
        print(f"Book '{title}' has been borrowed.")
    else: 
        print("This book is not available or does not exist in the database.")

def return_book():
    title = input("Enter the book you wish to return: ")
    if title in book_dict and not book_dict[title].is_available():
        book_dict[title].set_availability(True)
        print(f"This {title} has been returned to the library")
    else:
        print("This book was not borrowed or does not exist in the database")

def search_book():
    title = input("Enter the book you wish to search for: ")
    if title in book_dict:
        book_dict[title].display_info()
    else:
        print("Book is not in the library.")
    
def display_book():
    if not book_dict:
        print("No books in the library")
    else:
        for book in book_dict.values():
            book.display_info()

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
    
book_menu()