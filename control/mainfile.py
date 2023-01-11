from datetime import date
from model.client_file import Client
from model.Librarian_file import Librarian
from model.BorrowingOrder_file import BorrowingOrder
class MainFile:
    def __init__(self):
        self.clients_list = []
        self.librarians_list = []
        self.books_list = []
        self.borrowed_orders_list = []

    def add_client(self,client_id, client_name, client_age, client_id_no, client_phone):
        client = Client(client_id, client_name, client_age, client_id_no, client_phone)
        self.clients_list.append(client)

    def add_librarian(self, librarian_id, librarian_name, librarian_age, librarian_id_no, librarian_type):
        librarian = Librarian(librarian_id, librarian_name, librarian_age, librarian_id_no, librarian_type)
        self.librarians_list.append(librarian)

    def add_book(self, book):
        self.books_list.append(book)

    def add_borrowed_order(self, borrowed_order):
        self.borrowed_orders_list.append(borrowed_order)

    def search_order(self, order_id):
        for order in self.borrowed_orders_list:
            if order.id == order_id:
                return order



    def search_order(self, order_id):
        for order in self.borrowed_orders_list:
            if order.id == order_id:
                return order

    def check_book_status(self, book_id):
        for book in self.books_list:
            if book.id == book_id:
                return book.status

    def check_client(self, client_id):
        for client in self.clients_list:
            if client_id == client_id:
                return True
        return False

    def create_borrow_order(self, book_id, client_id):
        order_id = len(self.borrowed_orders_list) + 1
        order_date = date.today()
        order_status = 'Active'
        borrowed_order = BorrowingOrder(order_id, order_date, client_id, book_id, order_status)

        # Change book status
        for book in self.books_list:
            if book.id == book_id:
                book.book_status = "unavailable"
        self.add_borrowed_order(borrowed_order)

    def search_order(self, order_id):
        for order in self.borrowed_orders_list:
            if order.id == order_id:
                return order

    def show_all_orders(self):
        for order in self.borrowed_orders_list:
            print(order)