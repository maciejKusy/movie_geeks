from requests import get, exceptions
from ..constants.constant_values import IMDB_API_GENERAL_FILM_INFO_PATH, IMDB_API_GENERAL_SERIES_INFO_PATH,\
    IMDB_API_FULL_CAST_PATH
from .show_classes import Show, Film, Series


class ImdbApiDataRetriever:

    @classmethod
    def __handle_api_error(cls, error):
        print('API error!')

    @classmethod
    def retrieve_show_imdb_id(cls, show_instance: Show):
        api_path = str()
        if isinstance(show_instance, Film):
            api_path = IMDB_API_GENERAL_FILM_INFO_PATH
        elif isinstance(show_instance, Series):
            api_path = IMDB_API_GENERAL_SERIES_INFO_PATH

        general_info_api_path = f'{api_path}{show_instance.show_title} {show_instance.year_of_release}'
        try:
            show_data = get(general_info_api_path)
            show_data_dict = show_data.json()
            show_imdb_id = show_data_dict['results'][0]['id']
            return show_imdb_id
        except exceptions.RequestException as error:
            cls.__handle_api_error(error)

    @classmethod
    def retrieve_show_full_cast(cls, show_instance):
        show_id = cls.retrieve_show_imdb_id(show_instance)
        full_cast_api_path = f'{IMDB_API_FULL_CAST_PATH}{show_id}'
        full_cast_data = get(full_cast_api_path)
        full_cast_dict = full_cast_data.json()
        return full_cast_dict['actors']
