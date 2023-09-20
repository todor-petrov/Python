from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self. users_collection = []

    def register_user(self, username: str, age: int):
        ...

    def upload_movie(self, username: str, movie: Movie):
        ...

    def edit_movie(self,username: str, movie: Movie, ** kwargs):
        ...

    def delete_movie(self, username: str, movie: Movie):
        ...

    def like_movie(self, username: str, movie: Movie):
        ...

    def dislike_movie(self, username: str, movie: Movie):
        ...

    def display_movies(self):
        ...

    def __str__(self):
        all_users = '\n'.join(u.username for u in self.users_collection) \
            if self.users_collection else 'All users: No users.'
        all_movies = '\n'.join(m.title for m in self.movies_collection) \
            if self.movies_collection else 'All movies: No movies.'

