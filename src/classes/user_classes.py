from .manager_classes import ShowRepositoryManager
from .validator_classes import RatingValidator


class User:
    """
    Holds the basic info for a user such as id, the users ratings and a to-watch list.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_ratings = dict()
        self.to_watch_list = []

    @classmethod
    def __handle_value_error(cls, error):
        print(error)


class CommonUser(User):
    def __init__(self, user_id):
        super().__init__(user_id)
        self.user_id: str = user_id
        pass

    def rate_film(self, film_instance_string: str, user_rating: int):
        """
        Adds a rating of a particular value to a particular film in repository.
        :param film_instance_string: a str representation of a film.
        :param user_rating: the value of the user rating.
        :return: n/a
        """
        try:
            user_rating = RatingValidator.validate(user_rating)
            film_rated = ShowRepositoryManager.retrieve_film_from_repository(
                film_instance_string
            )

            self.add_rating(film_instance_string, film_rated.genre, user_rating)
            film_rated.add_rating(self.user_id, user_rating)
            film_rated.calculate_average_rating()

            ShowRepositoryManager.add_film_to_repository(film_rated)
            return
        except ValueError as error:
            self.__handle_value_error(error)

    def add_rating(self, show_instance_string: str, genre: str, rating: int):
        """
        Adds the user rating to the dict of all ratings for a particular user.
        :param show_instance_string: a str representation of a given show.
        :param genre: the genre of the show.
        :param rating: the value of the rating.
        :return: n/a
        """
        self.user_ratings.update(
            {show_instance_string: {"genre": genre, "rating": rating}}
        )

    def add_show_to_user_to_watch_list(self, show_instance_string):
        """
        Adds a str representation of a show to the user's 'to watch' list.
        :param show_instance_string:
        :return: n/a
        """
        self.to_watch_list.append(show_instance_string)
