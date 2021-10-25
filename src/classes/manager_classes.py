from .show_classes import Film, Series, Season, Episode
from pickle import dump, load
from os import listdir


class ShowRepositoryManager:

    def __init__(self):
        pass

    @classmethod
    def list_all_films_in_repository(cls):
        list_of_film_binary_files = listdir('show_repository/films')
        list_of_films = [film[0:-2:].title() for film in list_of_film_binary_files]
        return list_of_films

    @classmethod
    def list_all_series_in_repository(cls):
        list_of_series_binary_files = listdir('show_repository/series')
        list_of_series = [series[0:-2:] for series in list_of_series_binary_files]
        return list_of_series

    def create_film_and_add_to_repository(self, title: str, description: str, genre: str, year_of_release: int,
                                          director: str, duration_in_minutes: int):
        try:
            film_created = Film(title, description, genre, year_of_release, director, duration_in_minutes)
            if str(film_created) in self.list_all_films_in_repository():
                print('Film already in repository!')
                return
            else:
                self.__add_film_to_repository(film_created)
                print(f'{str(film_created)} saved to repository!')
                return
        except ValueError as error:
            print(error)

    def create_series_and_add_to_repository(self, title: str, description: str, genre: str, year_of_release: int,
                                            creator: str, number_of_seasons: int):
        try:
            series_created = Series(title, description, genre, year_of_release, creator, number_of_seasons)
            if str(series_created) in self.list_all_series_in_repository():
                print('Series already in repository!')
                return
            else:
                self.__add_series_to_repository(series_created)
                print(f'{str(series_created)} saved to repository!')
                return
        except ValueError as error:
            print(error)

    @classmethod
    def create_season_and_add_to_series(cls, series_instance: Series, season_number: int, number_of_episodes: int):
        try:
            season_created = Season(season_number, number_of_episodes)
            series_instance.seasons.append(season_created)
        except ValueError as error:
            print(error)

    @classmethod
    def create_episode_and_add_to_season(cls, season_instance: Season, episode_number: int, title: str, director: str,
                                         description: str):
        try:
            episode_created = Episode(episode_number, title, director, description)
            if str(episode_created) in season_instance.create_list_of_episodes():
                print('Episode with this number already present in this season!')
                return
            else:
                season_instance.episodes.append(episode_created)
        except ValueError as error:
            print(error)

    @classmethod
    def __add_film_to_repository(cls, film_object: Film):
        file_title = str(film_object)
        with open(f'show_repository/films/{file_title}.p', 'wb') as film_binary_file:
            dump(film_object, film_binary_file)

    @classmethod
    def __retrieve_film_from_repository(cls, film_instance_string: str):
        with open(f'show_repository/films/{film_instance_string}.p', 'rb') as film_binary_file:
            retrieved_film = load(film_binary_file)
            return retrieved_film

    @classmethod
    def __add_series_to_repository(cls, series_instance: Series):
        file_title = str(series_instance)
        with open(f'show_repository/series/{file_title}.p', 'wb') as series_binary_file:
            dump(series_instance, series_binary_file)

    @classmethod
    def __retrieve_series_from_repository(cls, series_instance_string: str):
        with open(f'show_repository/series/{series_instance_string}.p', 'rb') as series_binary_file:
            retrieved_series = load(series_binary_file)
            return retrieved_series
