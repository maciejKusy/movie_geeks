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

    def display_full_film_info(self):
        return f'{str(self)}\n' \
               f'{self.genre.capitalize()}\n' \
               f'Directed by: {self.director.title()}\n' \
               f'Duration: {self.duration_in_minutes} minutes\n' \
               f'Average rating: {self.average_rating}\n' \
               f'Rated {len(self.all_ratings)} times\n' \
               f'Short description:\n{self.description}\n'


class Series(Show):

    def __init__(self, show_title: str, description: str, genre: str, year_of_release: int, creator: str,
                 number_of_seasons: int):
        super().__init__(show_title, description, genre, year_of_release)
        self.creator = AuthorValidator.validate(creator)
        self.number_of_seasons = SeasonsNumberValidator.validate(number_of_seasons)
        self.seasons = []

    def create_printable_list_of_episodes(self):
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
