from .validator_classes import (
    AuthorValidator,
    DescriptionValidator,
    DurationValidator,
    EpisodesNumberValidator,
    GenreValidator,
    NumberValidator,
    SeasonsNumberValidator,
    TitleValidator,
    YearOfReleaseValidator,
)


class Show:
    """
    Holds all the attributes of a show (whether it's a film or a series). Also holds all the ratings that a given
    show has received along with the userID of the rating source (user) in a dict. Has a method for adding a rating
    and for re-calculating the average rating. The latter should be triggered whenever a rating is added which
    is handled by the CommonUser class.
    """

    def __init__(
        self,
        show_title: str,
        description: str,
        genre: str,
        year_of_release: int,
        all_ratings=None,
        average_rating=None,
    ):
        self.show_title: str = TitleValidator.validate(show_title)
        self.description: str = DescriptionValidator.validate(description)
        self.genre: str = GenreValidator.validate(genre)
        self.all_ratings: dict = dict() if all_ratings is None else all_ratings
        self.average_rating: float = 0 if average_rating is None else average_rating
        self.year_of_release: int = YearOfReleaseValidator.validate(year_of_release)

    def __str__(self) -> str:
        """
        Creates and returns a string representation of a Show. This is important as this is used for
        serializing the show instances and adding them to the show repository.
        :return: a string representation of a show.
        """
        return f"{self.show_title.title()} ({self.year_of_release})"

    def add_rating(self, user_id_of_rating_provider: str, rating_value: int):
        """
        Adds a rating to the rating dict of a particular Show instance.
        :param user_id_of_rating_provider: the user_id parameter of the CommonUser class instance that
        uses this method. This is done to store information on who added what rating inside the
        Show class instance for later reference.
        :param rating_value: the value of the rating.
        :return: n/a.
        """
        self.all_ratings.update({user_id_of_rating_provider: rating_value})

    def calculate_average_rating(self):
        """
        Uses the Shows dictionary of all ratings to calculate an average rating - pretty straightforward.
        :return: n/a.
        """
        self.average_rating = sum(self.all_ratings.values()) / len(
            self.all_ratings.values()
        )


class Film(Show):
    """
    A specific Show sub-class holding info characteristic to films as opposed to other types of shows.
    """

    def __init__(
        self,
        show_title: str,
        description: str,
        genre: str,
        year_of_release: int,
        director: str,
        duration_in_minutes: int,
        all_ratings=None,
        average_rating=None,
    ):
        super().__init__(
            show_title, description, genre, year_of_release, all_ratings, average_rating
        )
        self.director: str = AuthorValidator.validate(director)
        self.duration_in_minutes: int = DurationValidator.validate(duration_in_minutes)


class Series(Show):
    """
    A specific Show sub-class holding info characteristic to series as opposed to other types of shows.
    """

    def __init__(
        self,
        show_title: str,
        description: str,
        genre: str,
        year_of_release: int,
        creator: str,
        number_of_seasons: int,
        all_ratings=None,
        average_rating=None,
        seasons=None,
    ):
        super().__init__(
            show_title, description, genre, year_of_release, all_ratings, average_rating
        )
        self.creator: str = AuthorValidator.validate(creator)
        self.number_of_seasons: int = SeasonsNumberValidator.validate(number_of_seasons)
        self.seasons: list = [] if seasons is None else seasons

    def create_list_of_seasons(self):
        """
        Creates a list of all seasons present in a given series.
        :return: a list of all the seasons connected with a given series.
        """
        all_seasons = list()
        for season in self.seasons:
            all_seasons.append(str(season))
        return all_seasons


class Season:
    """
    Holds all the info relevant for a season of a series. The logic here is that an instance of Season is added
    to the list of seasons for a particular Series instance and then used to hold all the relevant info
    and a nested list of Episode instances.
    """

    def __init__(self, season_number: int, number_of_episodes: int, episodes=None):
        self.number: int = NumberValidator.validate(season_number)
        self.number_of_episodes: int = EpisodesNumberValidator.validate(
            number_of_episodes
        )
        self.episodes: list = [] if episodes is None else episodes

    def __str__(self):
        return f"Season {self.number}"

    def create_list_of_episodes(self):
        """
        Creates a list of all episodes present in a given season.
        :return: a list of all the episodes connected with a given season.
        """
        all_episodes = list()
        for episode in self.episodes:
            all_episodes.append(str(episode))
        return all_episodes


class Episode:
    """
    Holds all the info relevant for an episode of a series. When created, this is added to a Season instance's
    episode list.
    """

    def __init__(
        self, episode_number: int, episode_title: str, director: str, description: str
    ):
        self.number: int = NumberValidator.validate(episode_number)
        self.episode_title: str = TitleValidator.validate(episode_title)
        self.director: str = AuthorValidator.validate(director)
        self.description: str = DescriptionValidator.validate(description)

    def __str__(self):
        return f"Episode {self.number} - {self.episode_title.title()}"
