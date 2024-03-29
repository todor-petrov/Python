from unittest import TestCase, main
from project.trip import Trip


class TripTester(TestCase):
    def setUp(self):
        self.trip = Trip(10000.0, 3, True)

    def test_initialization(self):
        self.assertEqual(self.trip.budget, 10000.0)
        self.assertEqual(self.trip.travelers, 3)
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_travellers_number_is_more_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_is_correct(self):
        self.assertTrue(self.trip.is_family, True)
        self.trip.travelers = 1
        self.assertTrue(self.trip.is_family, False)

    def test_book_a_trip(self):
        destination = 'United Kingdom'
        message = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(message, self.trip.book_a_trip(destination))

    def test_book_trip_family_discount_happy_case(self):
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {'Bulgaria': 1350.0})
        self.assertEqual(self.trip.budget, 8650.0)
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 8650.00')

    def test_book_trip_no_family_discount(self):
        self.trip.travelers, self.trip.is_family = 1, False
        result = self.trip.book_a_trip('Bulgaria')
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {'Bulgaria': 500.0})
        self.assertEqual(self.trip.budget, 9500.0)
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 9500.00')

if 'name' == '__main__':
    main()
