from movie_app.movie_specification.movie import Movie
from movie_app.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):

        user = self._find_user_by_username(username)

        if user in self.users_collection:
            raise Exception('User already exists!')

        self.users_collection.append(User(username, age))
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):

        user = self._find_user_by_username(username)

        if user not in self.users_collection:
            raise Exception('This user does not exist!')

        if not movie.owner.username == username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if not movie.owner.username == username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for attribute, new_value in kwargs.items():
            setattr(movie, attribute, new_value)
        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):

        user = self._find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if not movie.owner.username == username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):

        user = self._find_user_by_username(username)

        if movie.owner.username == username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')

        if movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')

        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):

        user = self._find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f'{username} has not liked the movie {movie.title}!')

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{username} disliked {movie.title} movie.'

    def display_movies(self):

        if not self.movies_collection:
            return 'No movies found.'

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        movies = [m.details() for m in sorted_movies]
        return '\n'.join(movies)

    def __str__(self):

        users_movies_info = ['All users: ']

        if not self.users_collection:
            users_movies_info[0] += 'No users.'
        else:
            users_movies_info[0] += ', '.join(u.username for u in self.users_collection)

        users_movies_info.append('All movies: ')
        if not self.movies_collection:
            users_movies_info[1] += 'No movies.'
        else:
            users_movies_info[1] += ', '.join(m.title for m in self.movies_collection)

        return '\n'.join(users_movies_info)

    def _find_user_by_username(self, username):
        user = [u for u in self.users_collection if u.username == username]
        return user[0] if user else None
