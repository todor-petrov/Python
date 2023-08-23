from unittest import TestCase, main

from hash_map import HashMap


class TestHashMap(TestCase):

    def setUp(self) -> None:
        self.table = HashMap()

    def test_correct_initializing(self):
        self.assertEqual(4, self.table._HashMap__max_capacity)
        self.assertEqual([None] * 4, self.table._HashMap__keys)
        self.assertEqual([None] * 4, self.table._HashMap__values)

    def test__getitem__correct(self):
        self.table['name'] = 'Test'
        self.assertEqual('Test', self.table['name'])

    def test__getitem__non_existing_key_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table['name']
        self.assertEqual('name', str(ke.exception.args[0]))

    def test__setitem__replacing_existing_key(self):
        self.table['name'] = 'Test'
        self.table['name'] = 'New Test'
        self.assertEqual('New Test', self.table['name'])

    def test_resize_table_when_full(self):
        self.table['number1'] = 1
        self.table['number2'] = 1
        self.table['number3'] = 1
        self.table['number4'] = 1
        self.table['number5'] = 1

        self.assertEqual(8, self.table._HashMap__max_capacity)

    def test__setitem_collision(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 25
        self.assertEqual(2, self.table._HashMap__keys.index('age'))

    def test_setitem_linear_approach_starts_at_the_beginning_when_reaches_end(self):
        self.table['name'] = 'Peter'
        self.table['age'] = 25
        self.table['is_pet_owner'] = True
        self.assertEqual([None, 'name', 'age', 'is_pet_owner'], self.table._HashMap__keys)
        self.table['drives_car'] = False
        self.assertEqual(['drives_car', 'name', 'age', 'is_pet_owner'], self.table._HashMap__keys)

    def test_size_returns_only_occupied_places(self):
        self.table['name'] = 'Jack'
        self.assertEqual(1, self.table.size())

    def test_add_method_correct(self):
        self.table.add('name', 'Jack')
        self.assertIn('name', self.table._HashMap__keys)
        self.assertIn('Jack', self.table._HashMap__values)

    def test_get_method_correct(self):
        self.table['name'] = 'Jack'
        self.assertEqual('Jack', self.table.get('name'))

    def test_get_method_with_default_value_in_return(self):
        self.assertEqual(None, self.table.get('name'))
        self.assertEqual('Not found', self.table.get('name', 'Not found'))

    def test__str__(self):
        self.table['name'] = 'Jack'
        self.table['age'] = 29
        self.assertEqual('{name: Jack, age: 29}', str(self.table))

    def test__len__returns_max_capacity(self):
        self.assertEqual(4, len(self.table))


if __name__ == '__main__':
    main()