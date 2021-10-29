from abc import ABC, abstractmethod
from datetime import datetime
from ..constants.constant_values import (
    GENRES,
    TITLE_MAX_LENGTH,
    DESCRIPTION_MAX_LENGTH,
    AUTHOR_NAME_MAX_LENGTH,
    MAX_DURATION,
    MAX_SEASONS,
    MAX_EPISODES_PER_SEASON,
    YEAR_OF_FIRST_MOVIE,
    MINIMUM_RATING,
    MAXIMUM_RATING,
)


class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass


class TitleValidator(Validator):
    @classmethod
    def validate(cls, title: str) -> str:
        if isinstance(title, str) and len(title) <= TITLE_MAX_LENGTH:
            return title.lower()
        else:
            raise ValueError(
                f"The title must be a string and cannot exceed "
                f"{TITLE_MAX_LENGTH} characters!"
            )


class DescriptionValidator(Validator):
    @classmethod
    def validate(cls, description: str) -> str:
        if isinstance(description, str) and len(description) <= DESCRIPTION_MAX_LENGTH:
            return description
        else:
            raise ValueError(
                f"The description must be a string and cannot exceed "
                f"{DESCRIPTION_MAX_LENGTH} characters!"
            )


class GenreValidator(Validator):
    @classmethod
    def validate(cls, genre: str) -> str:
        if isinstance(genre, str) and genre.lower() in GENRES:
            return genre.lower()
        else:
            raise ValueError(
                f"The genre must be a string and one of the supported genres!"
            )


class AuthorValidator(Validator):
    @classmethod
    def validate(cls, author_name: str) -> str:
        if isinstance(author_name, str) and len(author_name) <= AUTHOR_NAME_MAX_LENGTH:
            return author_name.lower()
        else:
            raise ValueError(
                f"The author's name bust be a string and cannot exceed "
                f"{AUTHOR_NAME_MAX_LENGTH} characters!"
            )


class DurationValidator(Validator):
    @classmethod
    def validate(cls, duration: int) -> int:
        if isinstance(duration, int) and duration <= 1000:
            return duration
        else:
            raise ValueError(
                f"The duration must be an integer and cannot exceed " f"{MAX_DURATION}!"
            )


class SeasonsNumberValidator(Validator):
    @classmethod
    def validate(cls, number_of_seasons: int) -> int:
        if isinstance(number_of_seasons, int) and number_of_seasons <= MAX_SEASONS:
            return number_of_seasons
        else:
            raise ValueError(
                f"The number of seasons must be an integer and cannot exceed "
                f"{MAX_SEASONS}!"
            )


class EpisodesNumberValidator(Validator):
    @classmethod
    def validate(cls, number_of_episodes: int) -> int:
        if (
            isinstance(number_of_episodes, int)
            and number_of_episodes <= MAX_EPISODES_PER_SEASON
        ):
            return number_of_episodes
        else:
            raise ValueError(
                f"The number of episodes must be an integer and cannot exceed "
                f"{MAX_EPISODES_PER_SEASON}!"
            )


class NumberValidator(Validator):
    @classmethod
    def validate(cls, number: int) -> int:
        if isinstance(number, int):
            return number
        else:
            raise ValueError(f"The episode number must be an integer!")


class YearOfReleaseValidator(Validator):
    @classmethod
    def validate(cls, year_of_release: int) -> int:
        current_year = datetime.now().year
        if (
            isinstance(year_of_release, int)
            and YEAR_OF_FIRST_MOVIE <= year_of_release <= current_year
        ):
            return year_of_release
        else:
            raise ValueError(
                f"The year of release must be an integer and fall between {YEAR_OF_FIRST_MOVIE} and now."
            )


class RatingValidator(Validator):
    @classmethod
    def validate(cls, rating: int) -> int:
        if isinstance(rating, int) and MINIMUM_RATING <= rating <= MAXIMUM_RATING:
            return rating
        else:
            raise ValueError(
                f"The rating should be an integer between {MINIMUM_RATING} and {MAXIMUM_RATING}!"
            )
