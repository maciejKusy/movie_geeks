from .show_classes import Film, Series, Season, Episode
from json import dump, load
from os import listdir
from ..constants.constant_values import (
    STORAGE_FILE_EXTENSION,
    FILM_REPOSITORY_FOLDER_PATH,
    SERIES_REPOSITORY_FOLDER_PATH,
    GENRES,
    NUMBER_OF_RECOMMENDATIONS_TO_BE_DISPLAYED,
)
from typing import List, Dict


class FilmCreator:
    """
    Responsible for creating instances of Film class and passing them to the appropriate ShowRepositoryManager method
    for storage in the film repository.
    """
    @classmethod
    def create_film_and_add_to_repository(
        cls,
        title: str,
        description: str,
        genre: str,
        year_of_release: int,
        director: str,
        duration_in_minutes: int,
    ):
        """
        :param title: the title of a movie you want to create and add to repository;
        :param description: the description of the movie;
        :param genre: the genre of the movie - should be on the list of available genres (constant_values.GENRES);
        :param year_of_release: the year the film was released;
        :param director: the name of the director;
        :param duration_in_minutes: the duration of the movie expressed in minutes;
        :return: n/a - the objective of the method is to create a Film instance and pass it to the appropriate
        method for storage in repository in the form of a .json file;
        """
        try:
            film_created = Film(
                show_title=title,
                description=description,
                genre=genre,
                year_of_release=year_of_release,
                director=director,
                duration_in_minutes=duration_in_minutes,
            )
            if (
                str(film_created)
                in ShowRepositoryManager.list_all_films_in_repository()
            ):
                print("Film already in repository!")
                return
            else:
                ShowRepositoryManager.add_film_to_repository(film_created)
                print(f"{str(film_created)} saved to repository!")
                return
        except ValueError as error:
            print(error)


class SeriesCreator:
    """
    Responsible for creating instances of Series class and passing them to the appropriate ShowRepositoryManager method
    for storage in the film repository.
    """
    @classmethod
    def create_series_and_add_to_repository(
        cls,
        title: str,
        description: str,
        genre: str,
        year_of_release: int,
        creator: str,
        number_of_seasons: int,
    ):
        """
        :param title: the title of a series you want to create and add to repository;
        :param description: the description of the series;
        :param genre: the genre of the series - should be on the list of available genres (constant_values.GENRES);
        :param year_of_release: the year the series was first aired - the year the pilot episode came out;
        :param creator: the name of the creator of the series;
        :param number_of_seasons: the number of seasons - self-explanatory;
        :return: n/a - the objective of the method is to create a Series instance and pass it to the appropriate
        method for storage in repository in the form of a .json file;
        """
        try:
            series_created = Series(
                show_title=title,
                description=description,
                genre=genre,
                year_of_release=year_of_release,
                creator=creator,
                number_of_seasons=number_of_seasons,
            )
            if (
                str(series_created)
                in ShowRepositoryManager.list_all_series_in_repository()
            ):
                print("Series already in repository!")
                return
            else:
                ShowRepositoryManager.add_series_to_repository(series_created)
                print(f"{str(series_created)} saved to repository!")
                return
        except ValueError as error:
            print(error)


class SeasonCreator:
    """
    Responsible for creating an instance of the Season class and adding it to seasons list of a particular Series
    instance (passed as an argument).
    """
    @classmethod
    def create_season_and_add_to_series(
        cls,
        series_instance: Series,
        season_number: int,
        number_of_episodes: int
    ):
        """
        :param series_instance: a Series class instance that is to have a season added to it;
        :param season_number: the number of the season we're aiming to add;
        :param number_of_episodes: the number of episodes in that season;
        :return: n/a - the objective of the method is to append the list of seasons of a given Series;
        """
        try:
            season_created = Season(
                season_number=season_number,
                number_of_episodes=number_of_episodes
            )
            series_instance.seasons.append(season_created)
        except ValueError as error:
            print(error)


class EpisodeCreator:
    """
    Responsible for creating an instance of the Episode class and adding it to the episodes list of a given Season
    instance (passed as an argument).
    """
    @classmethod
    def create_episode_and_add_to_season(
        cls,
        season_instance: Season,
        episode_number: int,
        title: str,
        director: str,
        description: str,
    ):
        """
        :param season_instance: the Season instance that is to have an episode added to it;
        :param episode_number: the number of the episode to be added;
        :param title: the title of the episode;
        :param director: the full name of the director of the episode;
        :param description: the description of the episode, usually containing a quick summary of the plot;
        :return:
        """
        try:
            episode_created = Episode(
                episode_number=episode_number,
                episode_title=title,
                director=director,
                description=description,
            )
            if str(episode_created) in season_instance.create_list_of_episodes():
                print("Episode with this number already present in this season!")
                return
            else:
                season_instance.episodes.append(episode_created)
        except ValueError as error:
            print(error)


class ShowRepositoryManager:
    """
    Contains the logic for several basic operations on the show repository like adding or listing shows of
    a certain kind.
    """
    @classmethod
    def list_all_films_in_repository(cls) -> List[str]:
        """
        Uses the listdir library to list all the files in the film repository and then creates another (final)
        list of titles with the file extension removed;
        :return: a list of film titles available in the repository;
        """
        list_of_film_json_files = listdir(FILM_REPOSITORY_FOLDER_PATH)
        list_of_films = [
            film.rstrip(STORAGE_FILE_EXTENSION).title()
            for film in list_of_film_json_files
        ]
        return list_of_films

    @classmethod
    def list_all_series_in_repository(cls) -> List[str]:
        """
        Uses the listdir library to list all the files in the series repository and then creates another (final)
        list of titles with the file extension removed;
        :return: a list of series titles available in the repository;
        """
        list_of_series_json_files = listdir(SERIES_REPOSITORY_FOLDER_PATH)
        list_of_series = [
            series.rstrip(STORAGE_FILE_EXTENSION).title()
            for series in list_of_series_json_files
        ]
        return list_of_series

    @classmethod
    def add_film_to_repository(cls, film_instance: Film):
        """
        Creates a .json file in with the same title as the string representation of the Film instance and dumps the
        contents of the instance into the file using the json.dump() and vars() methods;
        :param film_instance: an instance of the Film class;
        :return: n/a
        """
        file_title = str(film_instance)
        with open(
            f"{FILM_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}", "w+"
        ) as film_json_file:
            dump(vars(film_instance), film_json_file)

    @classmethod
    def add_series_to_repository(cls, series_instance: Series):
        """
        Creates a .json file in with the same title as the string representation of the Series instance and dumps the
        contents of the instance into the file using the json.dump() and vars() methods;
        :param series_instance: an instance of the Series class;
        :return: n/a
        """
        file_title = str(series_instance)
        with open(
            f"{SERIES_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}", "w+"
        ) as series_json_file:
            dump(vars(series_instance), series_json_file)

    @classmethod
    def retrieve_film_from_repository(cls, film_instance_string: str) -> Film:
        """
        Takes the string representation of the Film instance as argument and retrieves from the film repository
        a file with a matching title. Uses the json.load() method to retrieve a dictionary of the instance parameters
        and re-instantiates the Film using Film(**parameters);
        :param film_instance_string: an instance of the Film class;
        :return: n/a
        """
        with open(
            f"{FILM_REPOSITORY_FOLDER_PATH}{film_instance_string}{STORAGE_FILE_EXTENSION}"
        ) as film_json_file:
            retrieved_film_json_dict = load(film_json_file)
            retrieved_film = Film(**retrieved_film_json_dict)
            return retrieved_film

    @classmethod
    def retrieve_series_from_repository(cls, series_instance_string: str) -> Series:
        """
        Takes the string representation of the Series instance as argument and retrieves from the series repository
        a file with a matching title. Uses the json.load() method to retrieve a dictionary of the instance parameters
        and re-instantiates the Series using Series(**parameters);
        :param series_instance_string: an instance of the Film class;
        :return: n/a
        """
        with open(
            f"{SERIES_REPOSITORY_FOLDER_PATH}{series_instance_string}{STORAGE_FILE_EXTENSION}"
        ) as series_json_file:
            retrieved_series_json_dict = load(series_json_file)
            retrieved_series = Series(**retrieved_series_json_dict)
            return retrieved_series


class ShowRepositoryViewer:
    """
    Responsible for basic viewing (in console at this point) operations on the Show repository.
    """
    @classmethod
    def view_all_films_in_repository(cls) -> str:
        """
        Iterates through a list of all the film titles available in film repository and adds them to the (initially
        empty) string, each one in new line;
        :return: string list of all available films;
        """
        printable_list_of_films = str()
        list_of_films_in_repository = (
            ShowRepositoryManager.list_all_films_in_repository()
        )
        for film in list_of_films_in_repository:
            printable_list_of_films += f"{film}\n"
        return printable_list_of_films

    @classmethod
    def view_all_series_in_repository(cls) -> str:
        """
        Iterates through a list of all the series titles available in series repository and adds them to the (initially
        empty) string, each one in new line;
        :return: string list of all available series;
        """
        printable_list_of_series = str()
        list_of_series_in_repository = (
            ShowRepositoryManager.list_all_series_in_repository()
        )
        for series in list_of_series_in_repository:
            printable_list_of_series += f"{series}\n"
        return printable_list_of_series

    @classmethod
    def retrieve_particular_film_info_from_repository(
            cls,
            film_instance_string: str
    ):
        """
        Retrieves a particular film from film repository and passes it as an argument to the method responsible
        for creating a string with full film info;
        :param film_instance_string: a string representation of a Film instance;
        :return: a string containing the full film info;
        """
        film_viewed = ShowRepositoryManager.retrieve_film_from_repository(
            film_instance_string
        )
        return cls.display_full_film_info(film_viewed)

    @classmethod
    def retrieve_particular_series_info_from_repository(
        cls,
        series_instance_string: str
    ):
        """
        Retrieves a particular series from series repository and passes it as an argument to the method responsible
        for creating a string with full series info;
        :param series_instance_string: a string representation of a Series instance;
        :return: a string containing the full series info;
        """
        series_viewed = ShowRepositoryManager.retrieve_series_from_repository(
            series_instance_string
        )
        return cls.display_full_series_info(series_viewed)

    @classmethod
    def display_full_film_info(cls, film_class_instance: Film) -> str:
        return (
            f"{str(film_class_instance)}\n"
            f"{film_class_instance.genre.capitalize()}\n"
            f"Directed by: {film_class_instance.director.title()}\n"
            f"Duration: {film_class_instance.duration_in_minutes} minutes\n"
            f"Average rating: {film_class_instance.average_rating}\n"
            f"Rated {len(film_class_instance.all_ratings)} times\n"
            f"Short description:\n{film_class_instance.description}\n"
        )

    @classmethod
    def display_full_series_info(cls, series_class_instance: Series) -> str:
        return (
            f"{str(series_class_instance)}\n"
            f"{series_class_instance.genre.capitalize()}\n"
            f"Created by: {series_class_instance.creator.title()}\n"
            f"Seasons: {series_class_instance.number_of_seasons}\n"
            f"Average rating: {series_class_instance.average_rating}\n"
            f"Rated {len(series_class_instance.all_ratings)} times\n"
            f"Short description: \n{series_class_instance.description}\n"
        )

    @classmethod
    def create_printable_list_of_episodes_for_series(
        cls, series_class_instance: Series
    ) -> str:
        episode_list = ""
        if series_class_instance.seasons:
            for season in series_class_instance.seasons:
                episode_list += f"{str(season)}\n"
                for episode in season.episodes:
                    episode_list += f"{str(episode)}\n"
            return episode_list


class RecommendationManager:
    @classmethod
    def create_preference_table_for_user(cls, user_class_instance) -> Dict[str, int]:
        preference_table = dict.fromkeys(GENRES, 0)
        for user_rating in user_class_instance.user_ratings:
            preference_table[
                user_class_instance.user_ratings[user_rating]["genre"]
            ] += user_class_instance.user_ratings[user_rating]["rating"]
        return preference_table

    @classmethod
    def create_recommendation_number_table_for_user(
        cls,
        preference_table: dict
    ) -> Dict[str, int]:
        sum_of_ratings = sum(preference_table.values())
        score_required_for_recommendation = round(
            sum_of_ratings / NUMBER_OF_RECOMMENDATIONS_TO_BE_DISPLAYED, 1
        )
        recommendation_number_table = dict()
        for genre, overall_rating in preference_table.items():
            if overall_rating > 0 and score_required_for_recommendation > 0:
                recommendation_number_table.update(
                    {genre: int(overall_rating // score_required_for_recommendation)}
                )
        return recommendation_number_table

    @classmethod
    def create_list_of_suggested_films_for_user(cls, user_class_instance) -> List[str]:
        preference_table = cls.create_preference_table_for_user(user_class_instance)
        recommendation_number_table = cls.create_recommendation_number_table_for_user(
            preference_table
        )
        suggested_films = list()
        list_of_all_films = ShowRepositoryManager.list_all_films_in_repository()

        cls.designate_films_to_be_added_to_recommendations(
            user_class_instance=user_class_instance,
            recommendation_number_table=recommendation_number_table,
            list_of_all_films=list_of_all_films,
            suggested_films=suggested_films
        )
        return suggested_films

    @classmethod
    def designate_films_to_be_added_to_recommendations(
            cls,
            user_class_instance,
            recommendation_number_table: Dict[str, int],
            list_of_all_films: List[str],
            suggested_films: List[str]
    ):
        for genre, number in recommendation_number_table.items():
            for n in range(number):
                for film in list_of_all_films:
                    if (
                        film in user_class_instance.user_ratings.keys()
                        or film in suggested_films
                    ):
                        pass
                    else:
                        film_object = (
                            ShowRepositoryManager.retrieve_film_from_repository(film)
                        )
                        if film_object.genre == genre:
                            suggested_films.append(film)
                            break

    @classmethod  # TO BE CHANGES
    def create_list_of_suggested_series_for_user(cls, user_class_instance) -> List[str]:
        preference_table = cls.create_preference_table_for_user(user_class_instance)
        recommendation_number_table = cls.create_recommendation_number_table_for_user(
            preference_table
        )
        suggested_series = list()
        list_of_all_series = ShowRepositoryManager.list_all_series_in_repository()

        cls.designate_series_to_be_added_to_recommendations(
            user_class_instance=user_class_instance,
            recommendation_number_table=recommendation_number_table,
            list_of_all_series=list_of_all_series,
            suggested_series=suggested_series
        )
        return suggested_series

    @classmethod
    def designate_series_to_be_added_to_recommendations(
            cls,
            user_class_instance,
            recommendation_number_table: Dict[str, int],
            list_of_all_series: List[str],
            suggested_series: List[str]
    ):
        for genre, number in recommendation_number_table.items():
            for n in range(number):
                for film in list_of_all_series:
                    if (
                            film in user_class_instance.user_ratings.keys()
                            or film in suggested_series
                    ):
                        pass
                    else:
                        film_object = (
                            ShowRepositoryManager.retrieve_film_from_repository(film)
                        )
                        if film_object.genre == genre:
                            suggested_series.append(film)
                            break
