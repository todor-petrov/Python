from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if any(u for u in self.users_collection if u.username == username):
            raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def __find_client(self, username: str):
        return next(filter(lambda u: u.username == username, self.users_collection), None)

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception("This user does not exist!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for current_movie in self.movies_collection:
            if current_movie.title == movie.title:
                raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_client(username)

        try:
            current_movie = next(filter(lambda m: m.title == movie.title, self.movies_collection))
        except StopIteration:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr_name, new_attr_name in kwargs.items():
            if attr_name == 'title':
                current_movie.title = new_attr_name
            elif attr_name == 'year':
                current_movie.year = new_attr_name
            elif attr_name == 'age_restriction':
                current_movie.age_restriction = new_attr_name

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_client(username)
        try:
            current_movie = next(filter(lambda m: m.title == movie.title, self.movies_collection))
        except StopIteration:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_client(username)

        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_client(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return 'No movies found.'

        return '\n'.join([m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))])

    def __str__(self):
        all_users_result = ', '.join([u.username for u in self.users_collection])
        all_movies_result = ', '.join([m.title for m in self.movies_collection])

        return f"All users: {all_users_result if self.users_collection else 'No users.'}\n" \
               f"All movies: {all_movies_result if self.movies_collection else 'No movies.'}"