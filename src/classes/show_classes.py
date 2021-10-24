from .validator_classes import TitleValidator, DescriptionValidator, GenreValidator, AuthorValidator, \
    DurationValidator, SeasonsNumberValidator, EpisodesNumberValidator, NumberValidator


class Show:

    def __init__(self, show_title: str, description: str, genre: str):
        self.title_ = TitleValidator.validate(show_title)
        self.description = DescriptionValidator.validate(description)
        self.genre = GenreValidator.validate(genre)
        self.average_score = 0


class Film(Show):

    def __init__(self, show_title: str, description: str, genre: str, director: str, duration_in_minutes: int):
        super().__init__(show_title, description, genre)
        self.director = AuthorValidator.validate(director)
        self.duration_in_minutes = DurationValidator.validate(duration_in_minutes)

    def __str__(self):
        return f'{self.title_.title()}\n' \
               f'{self.genre.title()}\n' \
               f'Directed by: {self.director.title()}\n' \
               f'Duration: {self.duration_in_minutes} minutes\n' \
               f'Description:\n{self.description}'


class Series(Show):

    def __init__(self, show_title: str, description: str, genre: str, creator: str, number_of_seasons: int):
        super().__init__(show_title, description, genre)
        self.creator = AuthorValidator.validate(creator)
        self.number_of_seasons = SeasonsNumberValidator.validate(number_of_seasons)
        self.seasons = []

    def __str__(self):
        return f'{self.title_.title()}\n' \
               f'Created by: {self.creator}\n' \
               f'Description: {self.description}\n' \
               f'No. of seasons: {self.number_of_seasons}\n' \
               f'List of episodes: {self.create_printable_episode_list()}'

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

    def __init__(self, season_number: int, number_of_episodes: int):
        self.number = NumberValidator.validate(season_number)
        self.number_of_episodes = EpisodesNumberValidator.validate(number_of_episodes)
        self.episodes = []


class Episode:

    def __init__(self, episode_title, director, description):
        self.episode_title = TitleValidator.validate(episode_title)
        self.director = AuthorValidator.validate(director)
        self.description = DescriptionValidator.validate(description)


