from unittest import TestCase, main
from project.team import Team


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team('Team')

    def test__init__method(self):
        self.assertEqual('Team', self.team.name)
        self.assertEqual({}, self.team.members)

    def test__init__method_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = 'Te@m'
        self.assertEqual('Team Name can contain only letters!', str(ve.exception))

    def test_add_method_adds_new_members_correctly(self):
        self.team.members = {'Member1': 20}
        result = self.team.add_member(Member1=25, Member2=21, Member3=22)
        self.assertDictEqual({'Member1': 20, 'Member2': 21, 'Member3': 22}, self.team.members)

    def test_add_method_without_new_members(self):
        result = self.team.add_member()
        self.assertEqual('Successfully added: ', result)

    def test_remove_member_returns_proper_message_if_member_does_not_exist(self):
        result = self.team.remove_member('Member')
        self.assertEqual('Member with name Member does not exist', result)

    def test_remove_member_removes_existing_member_and_returns_proper_message(self):
        self.team.members = {'Member1': 20, 'Member2': 21, 'Member3': 22}
        result = self.team.remove_member('Member2')
        self.assertEqual('Member Member2 removed', result)

    def test_remove_removes_last_member_removes_and_returns_proper_message(self):
        self.team.members = {'Member': 20}
        result = self.team.remove_member('Member')
        self.assertEqual({}, self.team.members)

    def test__gt__method_returns_correct_boolean(self):
        another = Team('Another')
        self.team.members = {'Member1': 20, 'Member2': 21}
        another.members = {'Member3': 22, 'Member4': 23, 'Member5': 24}
        self.assertEqual(False, self.team > another)
        self.assertEqual(True, self.team < another)

    def test__len__method_returns_correct_length(self):
        self.team.members = {'Member1': 20, 'Member2': 21}
        self.assertEqual(2, len(self.team))

    def test__add__method(self):
        self.another = Team('Another')
        self.team.members = {'Member1': 20, 'Member2': 21}
        self.another.members = {'Member3': 22, 'Member4': 23}
        result = self.team + self.another
        self.assertEqual('TeamAnother', result.name)
        self.assertEqual(4, len(result))
        self.assertDictEqual({'Member1': 20, 'Member2': 21, 'Member3': 22, 'Member4': 23}, result.members)

    def test__str__method(self):
        self.team.members = {'Member1': 20, 'Member2': 21}
        expected = 'Team name: Team\nMember: Member2 - 21-years old\nMember: Member1 - 20-years old'
        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    main()
