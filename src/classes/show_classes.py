from .validator_classes import TitleValidator, DescriptionValidator, GenreValidator, AuthorValidator, \
    DurationValidator, SeasonsNumberValidator, EpisodesNumberValidator, NumberValidator, YearOfReleaseValidator


class Show:

    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int):
        self.title_ = TitleValidator.validate(show_title)
        self.description = DescriptionValidator.validate(description)
        self.genre = GenreValidator.validate(genre)
        self.average_score = 0
        self.year_of_release = YearOfReleaseValidator.validate(year_of_release)


class Film(Show):

    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int, director: str,
                 duration_in_minutes: int):
        super().__init__(show_title, description, genre, year_of_release)
        self.director = AuthorValidator.validate(director)
        self.duration_in_minutes = DurationValidator.validate(duration_in_minutes)

    def __str__(self):
        return f'{self.title_.title()} ({self.year_of_release})'


class Series(Show):

    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int, creator: str,
                 number_of_seasons: int):
        super().__init__(show_title, description, genre, year_of_release)
        self.creator = AuthorValidator.validate(creator)
        self.number_of_seasons = SeasonsNumberValidator.validate(number_of_seasons)
        self.seasons = []

    def __str__(self):
        return f'{self.title_.title()} ({self.year_of_release}) - {self.number_of_seasons} seasons'

    def create_printable_episode_list(self):
        episode_list = ''
        if self.seasons:
            for season in self.seasons:
                episode_list += f'{str(season)}\n'
                for episode in season.episodes:
                    episode_list += f'{str(episode)}\n'
            return episode_list
        return


class Season:

    def __init__(self, season_number: int,
                 number_of_episodes: int):
        self.number = NumberValidator.validate(season_number)
        self.number_of_episodes = EpisodesNumberValidator.validate(number_of_episodes)
        self.episodes = []


class Episode:

    def __init__(self, episode_title: str,
                 director: str,
                 description: str):
        self.episode_title = TitleValidator.validate(episode_title)
        self.director = AuthorValidator.validate(director)
        self.description = DescriptionValidator.validate(description)
