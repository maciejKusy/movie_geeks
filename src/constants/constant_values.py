from typing import List

GENRES: List[str] = [
    "horror",
    "drama",
    "comedy",
    "crime thriller",
    "political thriller",
    "science-fiction",
    "fantasy",
    "psychological thriller",
    "sitcom",
    "documentary",
    "kids show",
    "romance",
    45,
    111,
]
TITLE_MAX_LENGTH: int = 100
DESCRIPTION_MAX_LENGTH: int = 200
AUTHOR_NAME_MAX_LENGTH: int = 50
MAX_DURATION: int = 1000
MAX_SEASONS: int = 50
MAX_EPISODES_PER_SEASON: int = 365
YEAR_OF_FIRST_MOVIE: int = 1888
MINIMUM_RATING: int = 1
MAXIMUM_RATING: int = 10
STORAGE_FILE_EXTENSION: str = ".json"
NUMBER_OF_RECOMMENDATIONS_TO_BE_DISPLAYED: int = len(GENRES)
FILM_REPOSITORY_FOLDER_PATH: str = "show_repository/films/"
SERIES_REPOSITORY_FOLDER_PATH: str = "show_repository/series/"
