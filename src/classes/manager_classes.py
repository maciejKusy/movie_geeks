from .show_classes import Film, Series, Season, Episode
from json import dump, load
from os import listdir
from ..constants.constant_values import STORAGE_FILE_EXTENSION, FILM_REPOSITORY_FOLDER_PATH, \
    SERIES_REPOSITORY_FOLDER_PATH, GENRES, NUMBER_OF_RECOMMENDATIONS_TO_BE_DISPLAYED


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
            dump(vars(film_instance), film_json_file)

    @classmethod
    def add_series_to_repository(cls, series_instance: Series):
        file_title = str(series_instance)
        with open(f'{SERIES_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}', 'w+') as series_json_file:
            dump(vars(series_instance), series_json_file)

    @classmethod
    def retrieve_film_from_repository(cls, film_instance_string: str):
        with open(f'{FILM_REPOSITORY_FOLDER_PATH}{film_instance_string}{STORAGE_FILE_EXTENSION}') as \
                film_json_file:
            retrieved_film_json_dict = load(film_json_file)
            retrieved_film = Film(**retrieved_film_json_dict)
            return retrieved_film

    @classmethod
    def retrieve_series_from_repository(cls, series_instance_string: str):
        with open(f'{SERIES_REPOSITORY_FOLDER_PATH}{series_instance_string}{STORAGE_FILE_EXTENSION}') as \
                series_json_file:
            retrieved_series_json_dict = load(series_json_file)
            retrieved_series = Series(**retrieved_series_json_dict)
            return retrieved_series


class ShowRepositoryViewer:

    @classmethod
    def view_all_films_in_repository(cls):
        list_of_films_in_repository = ShowRepositoryManager.list_all_films_in_repository()
        for film in list_of_films_in_repository:
            print(f'{film}\n')

    @classmethod
    def view_all_series_in_repository(cls):
        list_of_series_in_repository = ShowRepositoryManager.list_all_series_in_repository()
        for series in list_of_series_in_repository:
            print(f'{series}\n')

    @classmethod
    def view_particular_film_from_repository(cls, film_instance_string: str):
        film_viewed = ShowRepositoryManager.retrieve_film_from_repository(film_instance_string)
        print(cls.display_full_film_info(film_viewed))

    @classmethod
    def view_particular_series_from_repository(cls, series_instance_string: str):
        series_viewed = ShowRepositoryManager.retrieve_series_from_repository(series_instance_string)
        print(cls.display_full_series_info(series_viewed))

    @classmethod
    def display_full_film_info(cls, film_class_instance: Film):
        return f'{str(film_class_instance)}\n' \
               f'{film_class_instance.genre.capitalize()}\n' \
               f'Directed by: {film_class_instance.director.title()}\n' \
               f'Duration: {film_class_instance.duration_in_minutes} minutes\n' \
               f'Average rating: {film_class_instance.average_rating}\n' \
               f'Rated {len(film_class_instance.all_ratings)} times\n' \
               f'Short description:\n{film_class_instance.description}\n'

    @classmethod
    def display_full_series_info(cls, series_class_instance: Series):
        return f'{str(series_class_instance)}\n' \
               f'{series_class_instance.genre.capitalize()}\n' \
               f'Created by: {series_class_instance.creator.title()}\n' \
               f'Seasons: {series_class_instance.number_of_seasons}\n' \
               f'Average rating: {series_class_instance.average_rating}\n' \
               f'Rated {len(series_class_instance.all_ratings)} times\n' \
               f'Short description: \n{series_class_instance.description}\n'

    @classmethod
    def create_printable_list_of_episodes_for_series(cls, series_class_instance: Series):
        episode_list = ''
        if series_class_instance.seasons:
            for season in series_class_instance.seasons:
                episode_list += f'{str(season)}\n'
                for episode in season.episodes:
                    episode_list += f'{str(episode)}\n'
            return episode_list


class RecommendationManager:

    @classmethod
    def create_preference_table_for_user(cls, user_class_instance):
        preference_table = dict.fromkeys(GENRES, 0)
        for user_rating in user_class_instance.user_ratings:
            preference_table[user_class_instance.user_ratings[user_rating]['genre']] += \
                user_class_instance.user_ratings[user_rating]['rating']
        return preference_table

    @classmethod
    def create_recommendation_number_table_for_user(cls, preference_table: dict):
        sum_of_ratings = sum(preference_table.values())
        score_required_for_recommendation = round(sum_of_ratings / NUMBER_OF_RECOMMENDATIONS_TO_BE_DISPLAYED, 1)
        recommendation_number_table = dict()
        for genre, overall_rating in preference_table.items():
            if overall_rating > 0 and score_required_for_recommendation > 0:
                recommendation_number_table.update({genre: int(overall_rating // score_required_for_recommendation)})
        return recommendation_number_table

    @classmethod # TO BE CHANGED TO INCLUDE SERIES AS WELL!!!!
    def create_list_of_suggested_titles_for_user(cls, user_class_instance):
        preference_table = cls.create_preference_table_for_user(user_class_instance)
        recommendation_number_table = cls.create_recommendation_number_table_for_user(preference_table)
        suggested_films = list()
        list_of_all_films = ShowRepositoryManager.list_all_films_in_repository()

        for genre, number in recommendation_number_table.items():
            for n in range(number):
                for film in list_of_all_films:
                    if film in user_class_instance.user_ratings.keys() or film in suggested_films:
                        pass
                    else:
                        film_object = ShowRepositoryManager.retrieve_film_from_repository(film)
                        if film_object.genre == genre:
                            suggested_films.append(film)
                            break
        return suggested_films
