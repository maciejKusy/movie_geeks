from .show_classes import Film, Series
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

    def create_film_and_add_to_repository(self):
        try:
            title = input('Title:\n').lstrip().rstrip()
            description = input('Description:\n')
            genre = input('Genre:\n').lstrip().rstrip()
            year_of_release = int(input('Year of release:\n'))
            director = input('Director:\n')
            duration_in_minutes = int(input('Duration (minutes):\n'))

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

    def create_series_and_add_to_repository(self):
        try:
            title = input('Title:\n').lstrip().rstrip()
            description = input('Description:\n')
            genre = input('Genre:\n').lstrip().rstrip()
            year_of_release = int(input('Year of release:\n'))
            creator = input('Creator:\n')
            number_of_seasons = int(input('Number of seasons:\n'))

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

    def create_season_and_add_to_series(self):
        pass

    def create_episode_and_add_to_season(self):
        pass

    @classmethod
    def __add_film_to_repository(cls, film_object: Film):
        file_title = str(film_object)
        with open(f'show_repository/films/{file_title}.p', 'wb') as film_binary_file:
            dump(film_object, film_binary_file)

    @classmethod
    def __retrieve_film_from_repository(cls, film_class_obj_string: str):
        with open(f'show_repository/films/{film_class_obj_string}.p', 'rb') as film_binary_file:
            retrieved_film = load(film_binary_file)
            return retrieved_film

    @classmethod
    def __add_series_to_repository(cls, series_object: Series):
        file_title = str(series_object)
        with open(f'show_repository/series/{file_title}.p', 'wb') as series_binary_file:
            dump(series_object, series_binary_file)

    @classmethod
    def __retrieve_series_from_repository(cls, series_class_obj_string: str):
        with open(f'show_repository/series/{series_class_obj_string}.p', 'rb') as series_binary_file:
            retrieved_film = load(series_binary_file)
            return retrieved_film
