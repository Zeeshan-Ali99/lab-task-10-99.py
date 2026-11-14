# ==========================================
#       LIBRARY MANAGEMENT SYSTEM
# ==========================================

# Class to represent a book
class Book:

    # Constructor to initialize book details
    def _init_(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available = quantity


# Class to manage all library operations
class Library:

    def _init_(self):

        # Dictionary to store all book records
        self.books = {}

        # Dictionary to store issued book records
        self.issued_books = {}


    # 1. Function to add a new book
    def add_book(self):

        print("\n--- ADD NEW BOOK ---")

        # Get book information from the user
        book_id = input("Enter Book ID: ")

        # Check whether the book ID already exists
        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        # Get quantity and validate user input
        try:
            quantity = int(input("Enter Quantity: "))

            # Quantity must be a positive number
            if quantity <= 0:
                print("Quantity must be positive!")
                return

        except ValueError:
            print("Invalid quantity! Enter a whole number.")
            return

        # Create a book object and save it
        self.books[book_id] = Book(
            book_id, title, author, quantity
        )

        # Create an empty issued-book list
        self.issued_books[book_id] = []

        print("Book added successfully!")


    # 2. Function to display all books
    def view_books(self):

        print("\n--- ALL BOOKS ---")

        # Check whether the library contains books
        if not self.books:
            print("No books found!")
            return

        # Loop through all book records
        for book in self.books.values():

            print("----------------------")
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Total Quantity:", book.quantity)
            print("Available Quantity:", book.available)


    # 3. Function to search a book
    def search_book(self):

        print("\n--- SEARCH BOOK ---")

        # Take book ID or title from the user
        search = input("Enter Book ID or Title: ").lower()

        found = False

        # Search through all available book records
        for book in self.books.values():

            if (book.book_id.lower() == search or
                    search in book.title.lower()):

                print("----------------------")
                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available Quantity:", book.available)

                found = True

        # Display message if book does not exist
        if not found:
            print("Book not found!")


    # 4. Function to issue a book to a student
    def issue_book(self):

        print("\n--- ISSUE BOOK ---")

        book_id = input("Enter Book ID: ")

        # Check whether the book exists
        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        # Check available quantity before issuing
        if book.available <= 0:
            print("Book is not available!")
            return

        student = input("Enter Student Name: ")

        # Validate student name
        if student.strip() == "":
            print("Student name cannot be empty!")
            return

        # Save student name in issued-book records
        self.issued_books[book_id].append(student)

        # Decrease available book quantity
        book.available -= 1

        print("Book issued successfully!")
        print("Available Quantity:", book.available)


    # 5. Function to return an issued book
    def return_book(self):

        print("\n--- RETURN BOOK ---")

        book_id = input("Enter Book ID: ")

        # Check whether the book exists
        if book_id not in self.books:
            print("Book not found!")
            return

        student = input("Enter Student Name: ")

        # Check whether this student has borrowed this book
        if student not in self.issued_books[book_id]:
            print("Issued record not found!")
            return

        # Remove student from issued-book records
        self.issued_books[book_id].remove(student)

        # Increase available book quantity
        self.books[book_id].available += 1

        print("Book returned successfully!")
        print("Available Quantity:",
              self.books[book_id].available)


    # 6. Function to delete a book
    def delete_book(self):

        print("\n--- DELETE BOOK ---")

        book_id = input("Enter Book ID: ")

        # Check whether the book exists
        if book_id not in self.books:
            print("Book not found!")
            return

        # Do not delete a book if any copy is issued
        if self.issued_books[book_id]:
            print("Cannot delete! Book is currently issued.")
            return

        # Remove book from both dictionaries
        del self.books[book_id]
        del self.issued_books[book_id]

        print("Book deleted successfully!")


    # 7. Function to display currently issued books
    def view_issued_books(self):

        print("\n--- ISSUED BOOKS ---")

        found = False

        # Loop through issued book records
        for book_id, students in self.issued_books.items():

            # Display each student holding a book
            for student in students:

                book = self.books[book_id]

                print("----------------------")
                print("Book ID:", book.book_id)
                print("Book Title:", book.title)
                print("Student Name:", student)

                found = True

        # Display message if no books are issued
        if not found:
            print("No books are currently issued!")


# Main function to control the program
def main():

    # Create library object
    library = Library()

    # Keep the menu running until the user exits
    while True:

        # Display main menu
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. View Issued Books")
        print("8. Exit")

        # Get user's menu choice
        choice = input("Enter your choice: ")

        # Call the required function according to choice
        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.delete_book()

        elif choice == "7":
            library.view_issued_books()

        # Exit the program
        elif choice == "8":
            print("Thank you for using Library Management System!")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice! Please select 1 to 8.")


# Start the program from the main function
if _name_ == "_main_":
    main()