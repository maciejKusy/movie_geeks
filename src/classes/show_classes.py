from .validator_classes import (
    TitleValidator,
    DescriptionValidator,
    GenreValidator,
    AuthorValidator,
    DurationValidator,
    SeasonsNumberValidator,
    EpisodesNumberValidator,
    NumberValidator,
    YearOfReleaseValidator,
)
from typing import List


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
        return f"{self.show_title.title()} ({self.year_of_release})"

    def add_rating(self, user_id_of_rating_provider: str, rating_value: int):
        self.all_ratings.update({user_id_of_rating_provider: rating_value})

    def calculate_average_rating(self):
        self.average_rating = sum(self.all_ratings.values()) / len(
            self.all_ratings.values()
        )


class Film(Show):
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


class Season:
    def __init__(self, season_number: int, number_of_episodes: int):
        self.number: int = NumberValidator.validate(season_number)
        self.number_of_episodes: int = EpisodesNumberValidator.validate(
            number_of_episodes
        )
        self.episodes = []  # type: List[Episode]

    def __str__(self):
        return f"Season {self.number}"

    def create_list_of_episodes(self) -> List[str]:
        episode_list = []  # type: List[str]
        for episode in self.episodes:
            episode_list.append(str(episode))
        return episode_list


class Episode:
    def __init__(
        self, episode_number: int, episode_title: str, director: str, description: str
    ):
        self.number: int = NumberValidator.validate(episode_number)
        self.episode_title: str = TitleValidator.validate(episode_title)
        self.director: str = AuthorValidator.validate(director)
        self.description: str = DescriptionValidator.validate(description)

    def __str__(self):
        return f"Episode {self.number} - {self.episode_title}"
