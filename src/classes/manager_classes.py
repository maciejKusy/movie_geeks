from .show_classes import Film, Series, Season, Episode
from json import dump, dumps, load, loads
from os import listdir
from ..constants.constant_values import STORAGE_FILE_EXTENSION, FILM_REPOSITORY_FOLDER_PATH, \
    SERIES_REPOSITORY_FOLDER_PATH


class FilmCreator:

    @classmethod
    def create_film_and_add_to_repository(cls, title: str, description: str, genre: str, year_of_release: int,
                                          director: str, duration_in_minutes: int):
        try:
            film_created = Film(show_title=title, description=description, genre=genre, year_of_release=year_of_release,
                                director=director, duration_in_minutes=duration_in_minutes)
            if str(film_created) in ShowRepositoryManager.list_all_films_in_repository():
                print('Film already in repository!')
                return
            else:
                ShowRepositoryManager.add_film_to_repository(film_created)
                print(f'{str(film_created)} saved to repository!')
                return
        except ValueError as error:
            print(error)


class SeriesCreator:

    @classmethod
    def create_series_and_add_to_repository(cls, title: str, description: str, genre: str, year_of_release: int,
                                            creator: str, number_of_seasons: int):
        try:
            series_created = Series(show_title=title, description=description, genre=genre,
                                    year_of_release=year_of_release, creator=creator,
                                    number_of_seasons=number_of_seasons)
            if str(series_created) in ShowRepositoryManager.list_all_series_in_repository():
                print('Series already in repository!')
                return
            else:
                ShowRepositoryManager.add_series_to_repository(series_created)
                print(f'{str(series_created)} saved to repository!')
                return
        except ValueError as error:
            print(error)


class SeasonCreator:

    @classmethod
    def create_season_and_add_to_series(cls, series_instance: Series, season_number: int, number_of_episodes: int):
        try:
            season_created = Season(season_number=season_number, number_of_episodes=number_of_episodes)
            series_instance.seasons.append(season_created)
        except ValueError as error:
            print(error)


class EpisodeCreator:

    @classmethod
    def create_episode_and_add_to_season(cls, season_instance: Season, episode_number: int, title: str, director: str,
                                         description: str):
        try:
            episode_created = Episode(episode_number=episode_number, episode_title=title, director=director,
                                      description=description)
            if str(episode_created) in season_instance.create_list_of_episodes():
                print('Episode with this number already present in this season!')
                return
            else:
                season_instance.episodes.append(episode_created)
        except ValueError as error:
            print(error)


class ShowRepositoryManager:

    @classmethod
    def list_all_films_in_repository(cls):
        list_of_film_json_files = listdir(FILM_REPOSITORY_FOLDER_PATH)
        list_of_films = [film.rstrip(STORAGE_FILE_EXTENSION).title() for film in list_of_film_json_files]
        return list_of_films

    @classmethod
    def list_all_series_in_repository(cls):
        list_of_series_json_files = listdir(SERIES_REPOSITORY_FOLDER_PATH)
        list_of_series = [series.rstrip(STORAGE_FILE_EXTENSION).title() for series in list_of_series_json_files]
        return list_of_series

    @classmethod
    def add_film_to_repository(cls, film_instance: Film):
        file_title = str(film_instance)
        with open(f'{FILM_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}', 'w+') as film_json_file:
            film_json_string = dumps(film_instance.__dict__)
            dump(film_json_string, film_json_file)

    @classmethod
    def add_series_to_repository(cls, series_instance: Series):
        file_title = str(series_instance)
        with open(f'{SERIES_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}', 'w+') as series_json_file:
            series_json_string = dumps(series_instance.__dict__)
            dump(series_json_string, series_json_file)

    @classmethod
    def retrieve_film_from_repository(cls, film_instance_string: str):
        with open(f'{FILM_REPOSITORY_FOLDER_PATH}{film_instance_string}{STORAGE_FILE_EXTENSION}') as \
                film_json_file:
            retrieved_film_json = load(film_json_file)
            retrieved_film_json_dict = loads(retrieved_film_json)
            retrieved_film = Film(**retrieved_film_json_dict)
            return retrieved_film

    @classmethod
    def retrieve_series_from_repository(cls, series_instance_string: str):
        with open(f'{SERIES_REPOSITORY_FOLDER_PATH}{series_instance_string}{STORAGE_FILE_EXTENSION}') as \
                series_json_file:
            retrieved_series_json = load(series_json_file)
            retrieved_series_json_dict = loads(retrieved_series_json)
            retrieved_series = Series(**retrieved_series_json_dict)
            return retrieved_series


class ShowRepositoryViewer:

    @classmethod
    def view_all_films_in_repository(cls):
        list_of_films_in_repository = ShowRepositoryManager.list_all_films_in_repository()
        for film in list_of_films_in_repository:
            print(f'{film}\n')

    @classmethod
    def view_particular_film_from_repository(cls, film_instance_string: str):
        film_viewed = ShowRepositoryManager.retrieve_film_from_repository(film_instance_string)
        print(cls.display_full_film_info(film_viewed))

    @classmethod
    def display_full_film_info(cls, film_class_instance):
        return f'{str(film_class_instance)}\n' \
               f'{film_class_instance.genre.capitalize()}\n' \
               f'Directed by: {film_class_instance.director.title()}\n' \
               f'Duration: {film_class_instance.duration_in_minutes} minutes\n' \
               f'Average rating: {film_class_instance.average_rating}\n' \
               f'Rated {len(film_class_instance.all_ratings)} times\n' \
               f'Short description:\n{film_class_instance.description}\n'

    @classmethod
    def create_printable_list_of_episodes_for_series(cls, series_class_instance):
        episode_list = ''
        if series_class_instance.seasons:
            for season in series_class_instance.seasons:
                episode_list += f'{str(season)}\n'
                for episode in season.episodes:
                    episode_list += f'{str(episode)}\n'
            return episode_list
