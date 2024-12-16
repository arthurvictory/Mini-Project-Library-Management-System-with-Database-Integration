class AppControl:
    def main_menu():
        while True:
            print("""
               *=========================================*
                Welcome to the Library Management System
               *=========================================* 
                Main Menu:
                1. Book Operations
                2. User Operations
                3. Author Operations
                4. Quit
            """)

            menu = input("Enter a valid option: ")

            if menu == "1":
                import BookOperations
            elif menu == "2":
                import UserOperations
            elif menu == "3":
                import AuthorOperations
            elif menu == "4":
                print("Thanks for using our system! Goodbye.")
                break

    main_menu()