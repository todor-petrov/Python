# 01. Person
"""
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
"""


# 02. Mammal
"""
class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, mammal_type, sound):
        self.name = name
        self.type = mammal_type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    @staticmethod
    def get_kingdom():
        return __class__.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'
"""


# 03. Profile
"""
class Profile:

    MIN_PASSWORD_LENGTH = 8
    MIN_USERNAME_LENGTH = 5
    MAX_USERNAME_LENGTH = 15

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not Profile.MIN_USERNAME_LENGTH <= len(value) <= Profile.MAX_USERNAME_LENGTH:
            raise ValueError('The username must be between 5 and 15 characters.')
        else:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if (not Profile.MIN_PASSWORD_LENGTH <= len(value) or
                not any(s.isupper() for s in value) or
                not any(s.isdigit() for s in value)):
            raise ValueError('The password must be 8 or more characters'
                             ' with at least 1 digit and 1 uppercase letter.')
        else:
            self._password = value

    def __str__(self):
        return (f'You have a profile with username: "{self.username}" and '
                f'password: {"*" * len(self.password)}')
"""


# 04. Email Validator
"""
class EmailValidator:

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        parts = email.split('@')
        name = parts[0]
        mail, domain = parts[1].split('.')
        check_parts = [self.__is_name_valid(name),
                       self.__is_mail_valid(mail),
                       self.__is_domain_valid(domain)]
        return False not in check_parts
"""


# 05. Account
"""
class Account:
    def __init__(self, user_id, balance, pin):
        self.__id = user_id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return 'Wrong pin'

    def change_pin(self, old_pin, new_pin):
        if not old_pin == self.__pin:
            return 'Wrong pin'
        self.__pin = new_pin
        return 'Pin changed'


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
"""