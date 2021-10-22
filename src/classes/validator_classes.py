from abc import ABC, abstractmethod
from ..constants.constant_values import GENRES, TITLE_MAX_LENGTH, DESCRIPTION_MAX_LENGTH, AUTHOR_NAME_MAX_LENGTH,\
    MAX_DURATION, MAX_SEASONS, MAX_EPISODES_PER_SEASON


class Validator(ABC):

    @abstractmethod
    def validate(self, value):
        pass


class TitleValidator(Validator):

    @classmethod
    def validate(cls, title: str):
        if isinstance(title, str) and len(title) <= TITLE_MAX_LENGTH:
            return title
        else:
            raise ValueError(f'The title must be a string and cannot exceed '
                             f'{TITLE_MAX_LENGTH} characters!')


class DescriptionValidator(Validator):

    @classmethod
    def validate(cls, description: str):
        if isinstance(description, str) and len(description) <= DESCRIPTION_MAX_LENGTH:
            return description
        else:
            raise ValueError(f'The description must be a string and cannot exceed '
                             f'{DESCRIPTION_MAX_LENGTH} characters!')


class GenreValidator(Validator):

    @classmethod
    def validate(cls, genre: str):
        if isinstance(genre, str) and genre in GENRES:
            return genre
        else:
            raise ValueError(f'The genre must be a string and one of the supported genres!')


class AuthorValidator(Validator):

    @classmethod
    def validate(cls, author_name: str):
        if isinstance(author_name, str) and len(author_name) <= AUTHOR_NAME_MAX_LENGTH:
            return author_name
        else:
            raise ValueError(f'The author\'s name bust be a string and cannot exceed '
                             f'{AUTHOR_NAME_MAX_LENGTH} characters!')


class DurationValidator(Validator):

    @classmethod
    def validate(cls, duration: int):
        if isinstance(duration, int) and duration <= 1000:
            return duration
        else:
            raise ValueError(f'The duration must be an integer and cannot exceed '
                             f'{MAX_DURATION}!')


class SeasonsNumberValidator(Validator):

    @classmethod
    def validate(cls, number_of_seasons: int):
        if isinstance(number_of_seasons, int) and number_of_seasons <= MAX_SEASONS:
            return number_of_seasons
        else:
            raise ValueError(f'The number of seasons must be an integer and cannot exceed '
                             f'{MAX_DURATION}!')


class EpisodesNumberValidator(Validator):

    @classmethod
    def validate(cls, episodes_per_season: int):
        if isinstance(episodes_per_season, int) and episodes_per_season <= MAX_EPISODES_PER_SEASON:
            return episodes_per_season
        else:
            raise ValueError(f'The number of episodes per season must be an integer and cannot exceed '
                             f'{MAX_EPISODES_PER_SEASON}!')

