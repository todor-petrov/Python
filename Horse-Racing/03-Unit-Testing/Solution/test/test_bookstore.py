from unittest import TestCase, main
from project.bookstore import Bookstore


class BookStoreTests(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(10)
        self.store.availability_in_store_by_book_titles = {'Book 1': 3, 'Book 2': 4}

    def test__init__method(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertDictEqual({'Book 1': 3, 'Book 2': 4}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test__init__method_books_limit_setter_raises_if_limit_is_less_or_equal_than_0(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0
        self.assertEqual('Books limit of 0 is not valid', str(ve.exception))

    def test_correct__len__method(self):
        self.assertEqual(7, len(self.store))

    def test_receive_book_raises_if_not_enough_space(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Book 3', 5)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_receive_book_adds_new_book_with_numbers(self):
        result = self.store.receive_book('Book 3', 2)
        self.assertTrue(3, self.store.availability_in_store_by_book_titles['Book 1'])
        self.assertTrue(4, self.store.availability_in_store_by_book_titles['Book 2'])
        self.assertTrue(2, self.store.availability_in_store_by_book_titles['Book 3'])
        self.assertTrue(9, len(self.store))
        self.assertEqual('2 copies of Book 3 are available in the bookstore.', result)

    def test_receive_existing_book_and_updates_numbers(self):
        result = self.store.receive_book('Book 1', 1)
        self.assertTrue(4, self.store.availability_in_store_by_book_titles['Book 1'])
        self.assertTrue(4, self.store.availability_in_store_by_book_titles['Book 2'])
        self.assertTrue(8, len(self.store))
        self.assertEqual('4 copies of Book 1 are available in the bookstore.', result)

    def test_sell_book_raises_if_book_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Book 3', 8)
        self.assertEqual("Book Book 3 doesn't exist!", str(ex.exception))

    def test_sell_book_raises_if_book_has_not_enough_copies(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Book 1', 7)
        self.assertEqual('Book 1 has not enough copies to sell. Left: 3', str(ex.exception))

    def test_sell_book_returns_proper_message_and_updates_data(self):
        result = self.store.sell_book('Book 2', 3)
        self.assertEqual('Sold 3 copies of Book 2', result)
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual(3, self.store.availability_in_store_by_book_titles['Book 1'])
        self.assertEqual(1, self.store.availability_in_store_by_book_titles['Book 2'])
        self.assertEqual(4, len(self.store))
        self.store.sell_book('Book 2', 1)
        self.assertEqual(0, self.store.availability_in_store_by_book_titles['Book 2'])
        # Have to check if all copies are sold!!!

    def test__str__method(self):
        result = 'Total sold books: 0\nCurrent availability: 7\n - Book 1: 3 copies\n - Book 2: 4 copies'
        self.assertEqual(result, str(self.store))
        self.store.sell_book('Book 1', 2)
        result = 'Total sold books: 2\nCurrent availability: 5\n - Book 1: 1 copies\n - Book 2: 4 copies'
        self.assertEqual(result, str(self.store))


if __name__ == '__main__':
    main()