from .show_classes import Show, Film
from pickle import dump
from os import listdir


class RecordManager:

    def __init__(self):
        self.films = []
        self.series = []

    @classmethod
    def list_all_films_in_repository(cls):
        list_of_film_binary_files = listdir('show_repository/films')
        list_of_films = [film[0:-2:].title() for film in list_of_film_binary_files]
        return list_of_films

    def create_film_and_add_to_repository(self):
        try:
            title = input('Title:\n')
            description = input('Description:\n')
            genre = input('Genre:\n')
            director = input('Director:\n')
            duration_in_minutes = int(input('Duration (minutes):\n'))

            if title.title() in self.list_all_films_in_repository():
                print('Film already in repository!')
                return
            else:
                film_created = Film(title, description, genre, director, duration_in_minutes)
                self.save_show_as_binary_file(film_created)
                print(f'{film_created.title_.title()} saved to repository!')
                return
        except ValueError:
            print(ValueError)

    def create_series(self):
        pass

    def create_short_film(self):
        pass

    def create_season_and_add_to_series(self):
        pass

    def create_episode_and_add_to_season(self):
        pass

    @classmethod
    def save_show_as_binary_file(cls, show_object: Show):
        file_title = show_object.title_.title()
        with open(f'show_repository/films/{file_title}.p', 'wb') as show_binary_file:
            dump(show_object, show_binary_file)
