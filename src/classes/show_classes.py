from .validator_classes import TitleValidator, DescriptionValidator, GenreValidator, AuthorValidator, \
    DurationValidator, SeasonsNumberValidator, EpisodesNumberValidator, NumberValidator, YearOfReleaseValidator


class Show:
    """
    Holds all the attributes of a show (whether it's a film or a series). Also holds all the ratings that a given
    show has received along with the userID of the rating source (user) in a dict. Has a method for adding a rating
    and for re-calculating the average rating. The latter should be triggered whenever a rating is added which
    is handled by the CommonUser class.
    """
    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int):
        self.title_ = TitleValidator.validate(show_title)
        self.description = DescriptionValidator.validate(description)
        self.genre = GenreValidator.validate(genre)
        self.all_ratings = dict()
        self.average_rating = 0
        self.year_of_release = YearOfReleaseValidator.validate(year_of_release)

    def __str__(self):
        return f'{self.title_.title()} ({self.year_of_release})'

    def add_rating(self, user_id_of_rating_provider: str, rating_value: int):
        self.all_ratings.update({user_id_of_rating_provider: rating_value})

    def calculate_average_rating(self):
        self.average_rating = sum(self.all_ratings.values()) / len(self.all_ratings.values())


class Film(Show):

    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int, director: str,
                 duration_in_minutes: int):
        super().__init__(show_title, description, genre, year_of_release)
        self.director = AuthorValidator.validate(director)
        self.duration_in_minutes = DurationValidator.validate(duration_in_minutes)


class Series(Show):

    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int, creator: str,
                 number_of_seasons: int):
        super().__init__(show_title, description, genre, year_of_release)
        self.creator = AuthorValidator.validate(creator)
        self.number_of_seasons = SeasonsNumberValidator.validate(number_of_seasons)
        self.seasons = []


class Season:

    def __init__(self, season_number: int, number_of_episodes: int):
        self.number = NumberValidator.validate(season_number)
        self.number_of_episodes = EpisodesNumberValidator.validate(number_of_episodes)
        self.episodes = []

    def __str__(self):
        return f'Season {self.number}'

    def create_list_of_episodes(self):
        episode_list = []
        for episode in self.episodes:
            episode_list.append(str(episode))
        return episode_list


class Episode:

    def __init__(self, episode_number: int, episode_title: str, director: str, description: str):
        self.number = NumberValidator.validate(episode_number)
        self.episode_title = TitleValidator.validate(episode_title)
        self.director = AuthorValidator.validate(director)
        self.description = DescriptionValidator.validate(description)

    def __str__(self):
        return f'Episode {self.number} - {self.episode_title}'
