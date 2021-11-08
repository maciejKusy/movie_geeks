from typing import Dict

from requests import exceptions, get

from ..constants.constant_values import (IMDB_API_FULL_CAST_PATH,
                                         IMDB_API_GENERAL_FILM_INFO_PATH,
                                         IMDB_API_GENERAL_SERIES_INFO_PATH,
                                         IMDB_API_PLOT_SUMMARY_PATH)
from .show_classes import Film, Series, Show


class ImdbApiDataRetriever:
    """
    Houses the logic responsible for retrieving data from the IMDB API. The API key is stored in
    an environment variable stored in the .env file in project directory. This file - for obvious
    reasons - is not included in the remote repository but should be created locally.
    """

    @classmethod
    def __handle_api_error(cls, error: exceptions.RequestException):
        """
        Handles the errors that might occur during retrieval of data. This can obviously be made more elaborate
        but for now it merely prints the error.
        :param error: the exception raised during API data retrieval.
        :return: n/a
        """
        print(error)

    @classmethod
    def __retrieve_show_imdb_id(cls, show_instance: Show) -> str:
        """
        The IMDB API - when retrieving specific data for a show - requires that a IMDB-specific show ID
        is provided. This needs to first be retrieved using the show's title and year of release.
        :param show_instance: an instance of one of the Show superclass sub-classes.
        :return: a string that is the IMDB-specific show ID.
        """
        api_path = str()
        if isinstance(show_instance, Film):
            api_path = IMDB_API_GENERAL_FILM_INFO_PATH
        elif isinstance(show_instance, Series):
            api_path = IMDB_API_GENERAL_SERIES_INFO_PATH

        general_info_api_path = (
            f"{api_path}{show_instance.show_title} {show_instance.year_of_release}"
        )
        try:
            show_data = get(general_info_api_path)
            show_data_dict = show_data.json()
            if show_data_dict['results']:
                show_imdb_id = show_data_dict["results"][0]["id"]
                return show_imdb_id
            else:
                return str()
        except exceptions.RequestException as error:
            cls.__handle_api_error(error)

    @classmethod
    def retrieve_show_full_cast(cls, show_instance) -> Dict:
        """
        Based in the IMDB-specific show ID retrieves the full cast of a show.
        :param show_instance: an instance of one of the Show superclass sub-classes.
        :return: a dictionary containing information on which actor played whom in a given show.
        """
        show_id = cls.__retrieve_show_imdb_id(show_instance)
        full_cast_api_path = f"{IMDB_API_FULL_CAST_PATH}{show_id}"
        try:
            full_cast_data = get(full_cast_api_path)
            full_cast_dict = full_cast_data.json()
            return full_cast_dict["actors"]
        except exceptions.RequestException as error:
            cls.__handle_api_error(error)

    @classmethod
    def retrieve_show_plot_summary(cls, show_instance: Show) -> str:
        """
        Based in the IMDB-specific show ID retrieves the plot summary / description of a show.
        :param show_instance: an instance of one of the Show superclass sub-classes.
        :return: a dictionary containing information on which actor played whom in a given show.
        """
        show_id = cls.__retrieve_show_imdb_id(show_instance)
        plot_summary_api_path = f"{IMDB_API_PLOT_SUMMARY_PATH}{show_id}"
        try:
            plot_summary_data = get(plot_summary_api_path)
            plot_summary_string = plot_summary_data.json()
            return plot_summary_string["plot"]
        except exceptions.RequestException as error:
            cls.__handle_api_error(error)
