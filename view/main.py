from control.mainfile import MainFile
from model.client_file import Client
from model.Librarian_file import Librarian
from model.BorrowingOrder_file import BorrowingOrder
from model.Book_file import Book

main_file = MainFile() #instance
while True:
    # 0. Ask user to enter as a client or librarian
    user_type = input("Enter 'client' or 'librarian' else write exit:")
    if user_type == 'exit':
        break
    if user_type == 'client':
        client_id = input("Enter the client's ID: ")
        client_name = input("Enter the client's name: ")
        client_age = input("Enter the client's age: ")
        client_id_no = input("Enter the client's ID number: ")
        client_phone = input("Enter the client's phone number: ")
        main_file.add_client(client_id, client_name, client_age, client_id_no, client_phone)
        print("Client added to the system.")

        # 4. Show all books on system, then ask Librarian to borrow a book
        print("All Books: ")
        for book in main_file.books_list:
            print(book.title)

        # Ask which book to borrow
        book_id = input("Enter the ID of the book you want to borrow: ")

        # Check if the book is available for borrowing
        book_status = main_file.check_book_status(book_id)
        if book_status == "Available":
            # Ask for the client's ID number
            client_id = input("Enter the client's ID number: ")

            # Check if the client exists in the system
            client_exists = main_file.check_client(client_id)
            if client_exists:
                # Create a borrow_order with the selected book and the selected client
                main_file.create_borrow_order(book_id, client_id)
                print("Borrow order created successfully.")
            else:
                print("Client does not exist in the system.")
        else:
            print("Book is not available for borrowing.")

    elif user_type == 'librarian':
        librarian_id = input("Enter the librarian's ID: ")
        librarian_name = input("Enter the librarian's full name: ")
        librarian_age = input("Enter the librarian's age: ")
        librarian_id_no = input("Enter the librarian's ID number: ")
        librarian_type = input("Enter the librarian's employment type (Full/Part): ")
        main_file.add_librarian(librarian_id, librarian_name, librarian_age, librarian_id_no, librarian_type)
        print("Librarian added to the system.")

        books = []
        while True:
            book_id = input("Enter the ID of the book if you did not  more enters an empty string: ")
            if book_id == "":
                break
            if any(book.id == book_id for book in books):
                print("Book ID already exists. Please enter a different ID.")
                continue
            book_name = input("Enter the name of the book: ")
            book_desc = input("Enter the description of the book: ")
            book_author = input("Enter the author of the book: ")
            book_status = input("Enter the status of the book: ")
            books.append(Book(book_id, book_name, book_desc, book_author, book_status))

        for book in books:
            main_file.add_book(book)
        print("Books added to the system.")

        order_id = input("Enter the order id you want to search: ")
        result = main_file.search_order(order_id)
        if result:
            print(result)
        else:
            print("Order not found.")

        print("All Orders:")
        main_file.show_all_orders()