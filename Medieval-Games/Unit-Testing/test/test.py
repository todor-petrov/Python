from unittest import TestCase, main

from project.movie import Movie


class MovieTests(TestCase):

    def setUp(self) -> None:
        self.movie = Movie('Movie', 1990, 100)
        self.movie.actors = ['Actor 1', 'Actor 2', 'Actor 3']

    def test__init__method(self):
        self.assertEqual('Movie', self.movie.name)
        self.assertEqual(1990, self.movie.year)
        self.assertEqual(100, self.movie.rating)
        self.assertListEqual(['Actor 1', 'Actor 2', 'Actor 3'], self.movie.actors)

    def test__init__method_name_setter_raises_if_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test__init__method_year_setter_raises_if_year_is_less_than_min_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_method_appends_new_actor(self):
        self.movie.add_actor('Actor 4')
        self.assertListEqual(['Actor 1', 'Actor 2', 'Actor 3', 'Actor 4'], self.movie.actors)

    def test_add_actor_method_appends_existing_actor_returns_proper_string(self):
        self.movie.add_actor('Actor 2')
        self.assertEqual('Actor 2 is already added in the list of actors!', self.movie.add_actor('Actor 2'))

    def test__gt__method_returns_proper_string_when_other_rating_is_lower(self):
        other = Movie('Titanic', 1998, 90)
        self.assertEqual(f'"Movie" is better than "Titanic"', self.movie.__gt__(other))

    def test__gt__method_returns_proper_string_when_other_rating_is_bigger(self):
        other = Movie('Titanic', 1998, 120)
        self.assertEqual(f'"Titanic" is better than "Movie"', self.movie.__gt__(other))

    def test__repr__method_correct_data(self):
        result = self.movie.__repr__()
        expected = "Name: Movie\n" \
                   "Year of Release: 1990\n" \
                   "Rating: 100.00\n" \
                   "Cast: Actor 1, Actor 2, Actor 3"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
