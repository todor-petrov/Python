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


if 'name' == '__main__':
    main()
