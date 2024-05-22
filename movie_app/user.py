class User:

    MIN_AGE = 6

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < User.MIN_AGE:
            raise ValueError(f'Users under the age of {User.MIN_AGE} are not allowed!')
        self.__age = value

    def __str__(self):

        user_data = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']

        if self.movies_liked:
            user_data.extend([movie.details() for movie in self.movies_liked])
        else:
            user_data.append('No movies liked.')
        user_data.append('Owned movies:')

        if self.movies_owned:
            user_data.extend([movie.details() for movie in self.movies_owned])
        else:
            user_data.append('No movies owned.')

        return '\n'.join(user_data)
