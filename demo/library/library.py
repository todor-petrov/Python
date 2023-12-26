from user import User


class Library:

    def __init__(self):
        ...
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {book_name: 0}
            self.rented_books[user.username][book_name] = days_to_return
            self.books_available[author].remove(book_name)
            return f'{book_name} successfully rented for the next {days_to_return} days!'

        days_to_return = self.rented_books[user.username][book_name]
        return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

    def return_book(self, author:str, book_name:str, user: User):
        if book_name not in user.books:
            return f'{user.username} doesn\'t have this book in his/her records!'
        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)