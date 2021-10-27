from .validator_classes import RatingValidator
from .manager_classes import ShowRepositoryManager


class User:

    def __init__(self, user_id):
        self.user_id = user_id
        self.user_ratings = dict()
        self.to_watch_list = []


class CommonUser(User):

    def __init__(self, user_id):
        super().__init__(user_id)
        pass

    @classmethod
    def __handle_value_error(cls, error):
        print(error)

    def rate_film(self, film_instance_string: str, user_rating: int):
        try:
            user_rating = RatingValidator.validate(user_rating)
            film_rated = ShowRepositoryManager.retrieve_film_from_repository(film_instance_string)

            self.add_rating(film_instance_string, film_rated.genre, user_rating)
            film_rated.add_rating(self.user_id, user_rating)
            film_rated.calculate_average_rating()

            ShowRepositoryManager.add_film_to_repository(film_rated)
            return
        except ValueError as error:
            self.__handle_value_error(error)

    def add_rating(self, film_instance_string: str, genre: str, rating: int):
        self.user_ratings.update({film_instance_string: {'genre': genre, 'rating': rating}})

    def add_show_to_user_to_watch_list(self, show_instance_string):
        self.to_watch_list.append(show_instance_string)
