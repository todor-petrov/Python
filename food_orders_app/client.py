class Client:

    PHONE_NUMBER_LENGTH = 10

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value or not value.isdigit() or not value[0] == '0' or not len(value) == Client.PHONE_NUMBER_LENGTH:
            raise ValueError('Invalid phone number!')
        self.__phone_number = value
