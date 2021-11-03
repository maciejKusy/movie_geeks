from os import listdir
from pickle import dump, load
from typing import Dict, List

from ..constants.constant_values import (
    FILM_REPOSITORY_FOLDER_PATH, GENRES,
    NUMBER_OF_RECOMMENDATIONS_TO_BE_DISPLAYED, SERIES_REPOSITORY_FOLDER_PATH,
    STORAGE_FILE_EXTENSION)
from .api_data_retrieval_classes import ImdbApiDataRetriever
from .show_classes import Episode, Film, Season, Series, Show


class Creator:
    @classmethod
    def handle_value_error(cls, error: ValueError):
        print(error)


class FilmCreator(Creator):
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
        method for storage in repository in the form of a .p file;
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
            super().handle_value_error(error)


class SeriesCreator(Creator):
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
        method for storage in repository in the form of a .p file;
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
            super().handle_value_error(error)


class SeasonCreator(Creator):
    """
    Responsible for creating an instance of the Season class and adding it to seasons list of a particular Series
    instance (passed as an argument).
    """

    @classmethod
    def create_season_and_add_to_series(
        cls, series_instance: Series, season_number: int, number_of_episodes: int
    ):
        """
        :param series_instance: a Series class instance that is to have a season added to it;
        :param season_number: the number of the season we're aiming to add;
        :param number_of_episodes: the number of episodes in that season;
        :return: n/a - the objective of the method is to append the list of seasons of a given Series;
        """
        try:
            season_created = Season(
                season_number=season_number, number_of_episodes=number_of_episodes
            )
            if str(season_created) in series_instance.create_list_of_seasons():
                print("Season with this number already present in this series!")
                return
            else:
                series_instance.seasons.append(season_created)
        except ValueError as error:
            super().handle_value_error(error)


class EpisodeCreator(Creator):
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
            super().handle_value_error(error)


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
        Creates a .p file in with the same title as the string representation of the Film instance and dumps the
        contents of the instance into the file using the pickle.dump() and vars() methods;
        :param film_instance: an instance of the Film class;
        :return: n/a
        """
        file_title = str(film_instance)
        with open(
            f"{FILM_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}", "wb+"
        ) as film_binary_file:
            dump(film_instance, film_binary_file)

    @classmethod
    def add_series_to_repository(cls, series_instance: Series):
        """
        Creates .p file in with the same title as the string representation of the Series instance and dumps the
        contents of the instance into the file using the pickle.dump() and vars() methods;
        :param series_instance: an instance of the Series class;
        :return: n/a
        """
        file_title = str(series_instance)
        with open(
            f"{SERIES_REPOSITORY_FOLDER_PATH}{file_title}{STORAGE_FILE_EXTENSION}",
            "wb+",
        ) as series_binary_file:
            dump(series_instance, series_binary_file)

    @classmethod
    def retrieve_film_from_repository(cls, film_instance_string: str) -> Film:
        """
        Takes the string representation of the Film instance as argument and retrieves from the film repository
        a file with a matching title. Uses the pickle.load() method to retrieve a dictionary of the instance parameters
        and re-instantiates the Film using Film(**parameters);
        :param film_instance_string: an instance of the Film class;
        :return: n/a
        """
        with open(
            f"{FILM_REPOSITORY_FOLDER_PATH}{film_instance_string}{STORAGE_FILE_EXTENSION}",
            "rb",
        ) as film_binary_file:
            retrieved_film = load(film_binary_file)
            return retrieved_film

    @classmethod
    def retrieve_series_from_repository(cls, series_instance_string: str) -> Series:
        """
        Takes the string representation of the Series instance as argument and retrieves from the series repository
        a file with a matching title. Uses the pickle.load() method to retrieve a dictionary of the instance parameters
        and re-instantiates the Series using Series(**parameters);
        :param series_instance_string: an instance of the Film class;
        :return: n/a
        """
        with open(
            f"{SERIES_REPOSITORY_FOLDER_PATH}{series_instance_string}{STORAGE_FILE_EXTENSION}",
            "rb",
        ) as series_binary_file:
            retrieved_series = load(series_binary_file)
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
    def display_full_film_info(cls, film_class_instance: Film) -> str:
        """
        Returns a string that contains all the relevant info for a particular film.
        :param film_class_instance: An instance of the Film class.
        :return: a string containing full film info.
        """
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
        """
        Returns a string that contains all the relevant info for a particular series.
        :param series_class_instance: An instance of the Series class.
        :return: a string containing full series info.
        """
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
        """
        Creates a printable (in the console) list of episodes for a given series instance.
        :param series_class_instance: An instance of the Series class.
        :return: A string containing the list.
        """
        episode_list = ""
        if series_class_instance.seasons:
            for season in series_class_instance.seasons:
                episode_list += f"{str(season)}\n"
                for episode in season.episodes:
                    episode_list += f"{str(episode)}\n"
            return episode_list

    @classmethod
    def create_printable_full_cast_info_for_show(cls, show_instance: Show) -> str:
        """
        Interacts with the class responsible for data retrieval from
        :param show_instance: an instance of the Show parent class.
        :return: a string representation of the full cast of a given show.
        """
        full_cast_dict = ImdbApiDataRetriever.retrieve_show_full_cast(show_instance)
        full_cast_string = str()
        for actor in full_cast_dict:
            full_cast_string += f'{actor["name"]} as {actor["asCharacter"]}\n'
        return full_cast_string


class RecommendationManager:
    """
    Class responsible for the logic of creating recommendations for users based on their ratings.
    """

    @classmethod
    def __create_preference_table_for_user(cls, user_class_instance) -> Dict[str, int]:
        """
        Creates a 'preference table' - that is a dictionary that contains the sums of all user ratings for
        a particular genre and assigns these sums to their respective genres.
        :param user_class_instance: an instance of the CommonUser class;
        :return: a dictionary whose keys are the available genres and values are the sums of user
        ratings for a given genre.
        """
        preference_table = dict.fromkeys(GENRES, 0)
        for user_rating in user_class_instance.user_ratings:
            preference_table[
                user_class_instance.user_ratings[user_rating]["genre"]
            ] += user_class_instance.user_ratings[user_rating]["rating"]
        return preference_table

    @classmethod
    def __create_recommendation_number_table_for_user(
        cls, preference_table: dict
    ) -> Dict[str, int]:
        """
        Creates a table containing the number of recommendations for a given user based on their preference
        table. It takes into account the maximum number of recommendations (by default it is the len() of
        the genre list) and defines a minimum amount of rating 'points' a genre needs to have in order to
        warrant one recommendation. This is done basically by dividing the sum of all ratings by the max number of
        recommendations.
        :param preference_table: a dictionary whose keys are the available genres and values are the sums of user
        ratings for a given genre.
        :return: a dictionary whose keys are the available genres and the values represent the number of
        recommendations to be included for every genre.
        """
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
    def __create_film_ratings_table(cls) -> Dict:
        """
        Iterates through film titles available in the film repository and creates a dict of films with their
        average scores.
        :return: Dictionary where the keys are the film string representations and the values are the films'
        average ratings.
        """
        list_of_all_films = ShowRepositoryManager.list_all_films_in_repository()
        ratings_table = dict()
        for film in list_of_all_films:
            film_instance = ShowRepositoryManager.retrieve_film_from_repository(film)
            ratings_table.update(
                {
                    film: {
                        "rating": film_instance.average_rating,
                        "genre": film_instance.genre,
                    }
                }
            )
        return ratings_table

    @classmethod
    def __create_film_ranking(cls) -> Dict:
        """
        Creates the ratings table for all available films, converts it to it's .items() list and then sorts the list
        using a custom key which is the [1]['rating'] indexed item in the pair - the film rating, so the ranking itself,
        thus creating a dictionary sorted based on the rating itself. The reverse argument is true due to the fact that
        we want the highest values at the beginning of this dictionary.
        :return: a dictionary containing films sorted from the highest rating to the lowest.
        """
        ratings_table = cls.__create_film_ratings_table()
        sorted_ratings = sorted(
            ratings_table.items(), key=lambda x: x[1]["rating"], reverse=True
        )
        film_ranking = dict()
        for rating in sorted_ratings:
            film_ranking.update(
                {
                    rating[0]: {
                        "rating": rating[1]["rating"],
                        "genre": rating[1]["genre"],
                    }
                }
            )
        return film_ranking

    @classmethod
    def __create_series_ratings_table(cls) -> Dict:
        """
        Iterates through series titles available in the series repository and creates a dict of series with their
        average scores.
        :return: Dictionary where the keys are the series string representations and the values are the series'
        average ratings.
        """
        list_of_all_series = ShowRepositoryManager.list_all_series_in_repository()
        ratings_table = dict()
        for series in list_of_all_series:
            series_instance = ShowRepositoryManager.retrieve_series_from_repository(
                series
            )
            ratings_table.update(
                {
                    series: {
                        "rating": series_instance.average_rating,
                        "genre": series_instance.genre,
                    }
                }
            )
        return ratings_table

    @classmethod
    def __create_series_ranking(cls) -> Dict:
        """
        Creates the ratings table for all available series, converts it to it's .items() list and then sorts the list
        using a custom key which is the [1]['rating'] indexed item in the pair - the series rating,
        thus creating a dictionary sorted based on the rating itself. The reverse argument is true due to the fact that
        we want the highest values at the beginning of this dictionary.
        :return: a dictionary containing series' sorted from the highest rating to the lowest.
        """
        ratings_table = cls.__create_series_ratings_table()
        sorted_ratings = sorted(
            ratings_table.items(), key=lambda x: x[1]["rating"], reverse=True
        )
        series_ranking = dict()
        for rating in sorted_ratings:
            series_ranking.update(
                {
                    rating[0]: {
                        "rating": rating[1]["rating"],
                        "genre": rating[1]["genre"],
                    }
                }
            )
        return series_ranking

    @classmethod
    def create_list_of_suggested_films_for_user(cls, user_class_instance) -> List[str]:
        """
        Creates the list of recommended titles for a given user based on their ratings. Utilizes the preference table
        and recommendations table from separate methods.
        :param user_class_instance: an instance of the CommonUser class.
        :return: a list of suggested films.
        """
        preference_table = cls.__create_preference_table_for_user(user_class_instance)
        recommendation_number_table = cls.__create_recommendation_number_table_for_user(
            preference_table
        )
        film_ranking = cls.__create_film_ranking()
        suggested_films = list()

        cls.__designate_shows_to_be_added_to_recommendations(
            user_class_instance=user_class_instance,
            recommendation_number_table=recommendation_number_table,
            ranking=film_ranking,
            suggested_shows=suggested_films,
        )
        return suggested_films

    @classmethod
    def create_list_of_suggested_series_for_user(cls, user_class_instance) -> List[str]:
        """
        Creates the list of recommended titles for a given user based on their ratings. Utilizes the preference table
        and recommendations table from separate methods.
        :param user_class_instance: an instance of the CommonUser class.
        :return: a list of suggested series.
        """
        preference_table = cls.__create_preference_table_for_user(user_class_instance)
        recommendation_number_table = cls.__create_recommendation_number_table_for_user(
            preference_table
        )
        series_ranking = cls.__create_series_ranking()
        suggested_series = list()

        cls.__designate_shows_to_be_added_to_recommendations(
            user_class_instance=user_class_instance,
            recommendation_number_table=recommendation_number_table,
            ranking=series_ranking,
            suggested_shows=suggested_series,
        )
        return suggested_series

    @classmethod
    def __designate_shows_to_be_added_to_recommendations(
        cls,
        user_class_instance,
        recommendation_number_table: Dict[str, int],
        ranking: dict,
        suggested_shows: List[str],
    ):
        """
        Uses the show ranking and the user's recommendation number table to provide recommendations
        of the highest ranked shows that have the desired genre.
        :param user_class_instance: an instance of the CommonUser class.
        :param recommendation_number_table: the dictionary containing genre: number_of_recommendations_due pairs.
        :param ranking: the overall ratings ranking of all available shows.
        :param suggested_shows: an empty list that is populated by this method.
        :return: a list of titles recommended for a given user.
        """
        all_shows_rated_by_user = user_class_instance.user_ratings.keys()
        for genre, number in recommendation_number_table.items():
            for n in range(number):
                for show in ranking.keys():
                    if show in all_shows_rated_by_user or show in suggested_shows:
                        pass
                    else:
                        if ranking[show]["genre"] == genre:
                            suggested_shows.append(show)
                            break
