from .manager_classes import (FilmCreator, RecommendationManager,
                              SeriesCreator, ShowRepositoryManager,
                              ShowRepositoryViewer)
from .user_classes import CommonUser


class FeatureDemonstrationManager:
    @classmethod
    def demo_film_rating_process(cls):
        """
        This method demonstrates - by printing to the console - the process of rating Shows (films in this case)
        present in the film repository.
        :return: n/a
        """
        # First off, let's create two films and save them to the film repository serialized as
        # binary files:
        FilmCreator.create_film_and_add_to_repository(
            "Casablanca", "drama", 1948, "michael curtiz", 102
        )
        FilmCreator.create_film_and_add_to_repository(
            "Hungover", "comedy", 2006, "some guy", 92
        )

        # Next, let's create a couple of CommonUser class instances and have them rate the movies
        # we just created:
        user1 = CommonUser("Rodrigo6969")
        user1.rate_film("Casablanca (1948)", 10)
        user1.rate_film("Hungover (2006)", 5)
        user2 = CommonUser("DramaQueen")
        user2.rate_film("Casablanca (1948)", 5)
        user2.rate_film("Hungover (2006)", 9)
        user3 = CommonUser("SilentBob")
        user3.rate_film("Casablanca (1948)", 20)
        user3.rate_film("Hungover (2006)", 2)

        # Now we want to access the properties of a given movie so let's retrieve it from the repository:
        casablanca = ShowRepositoryManager.retrieve_film_from_repository(
            "Casablanca (1948)"
        )
        print(casablanca.average_rating)

        # Let's also see what ratings have been added to each individual user's ratings list:
        print(user1.user_ratings)
        print(user2.user_ratings)
        print(user3.user_ratings)

    @classmethod
    def demo_recommendations_creation_process(cls):
        """
        This method demonstrates - by printing to the console - the process of creating a list of recommended
        titles for a given user based on their ratings. The highest rated genre in a user's ratings
        dict gets the most recommendations and the best rated titles are recommended in the first place above lower
        rated ones.
        :return: n/a
        """
        # First, let's create a couple of Series titles and store them in the repository:
        SeriesCreator.create_series_and_add_to_repository(
            "friends", "comedy", 1994, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "louie", "comedy", 2004, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "the store", "comedy", 1989, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "comedy series 4", "comedy", 1999, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "comedy series 5", "comedy", 1999, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "limps", "comedy", 2018, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "little women", "drama", 2002, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "the court", "drama", 1997, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "sitdown", "sitcom", 2007, "some guy", 7
        )

        # Next, let's create some users and have them rate some of the series present in the repository:
        user1 = CommonUser("Rodrigo6969")
        user2 = CommonUser("Birdman")
        user1.rate_series("Friends (1994)", 10)
        user1.rate_series("Louie (2004)", 8)
        user1.rate_series("The Store (1989)", 7)
        user2.rate_series("Limps (2018)", 10)

        # Lastly, let's see what titles are recommended to the user who rated a comedy series highly:
        print(RecommendationManager.create_list_of_suggested_series_for_user(user2))

    @classmethod
    def demo_show_creation_process(cls):
        """
        The below method demos the process of creating Films and Series and adding them to to the
        show repository in the form of binary files.
        :return: n/a
        """
        FilmCreator.create_film_and_add_to_repository(
            "comedy 3", "comedy", 2003, "some gal", 92
        )
        FilmCreator.create_film_and_add_to_repository(
            "comedy 4", "comedy", 2010, "some dir", 107
        )
        FilmCreator.create_film_and_add_to_repository(
            "comedy 5", "comedy", 1995, "the dude", 99
        )
        SeriesCreator.create_series_and_add_to_repository(
            "comedy series 1", "comedy", 1999, "some guy", 7
        )
        SeriesCreator.create_series_and_add_to_repository(
            "comedy series 2", "comedy", 1989, "some guy", 3
        )
        SeriesCreator.create_series_and_add_to_repository(
            "comedy series 3", "comedy", 1979, "some guy", 5
        )

    @classmethod
    def demo_retrieving_full_cast_from_imdb_api(cls):
        """
        This method demonstrates how the program retrieves a list of full cast for a particular show.
        The list is printed in the console.
        :return: n/a
        """
        # First, creating a film and adding it to the repository:
        FilmCreator.create_film_and_add_to_repository(
            "interstellar",
            "science-fiction",
            2014,
            "christopher nolan",
            120,
        )

        # Then, let's retrieve the film from the repository (deserialize the binary file) and assign it
        # to a variable:
        interstellar = ShowRepositoryManager.retrieve_film_from_repository(
            "Interstellar (2014)"
        )

        # Lastly, let's print our the result of retrieving the full cast for a given show:
        print(
            ShowRepositoryViewer.create_printable_full_cast_info_for_show(interstellar)
        )

    @classmethod
    def demo_viewing_full_data_for_show(cls):
        """
        This method demonstrates the feature of displaying full show info for a given Show class instance.
        :return: n/a
        """
        FilmCreator.create_film_and_add_to_repository(
            "dune", "science-fiction", 2021, "denis villeneuve", 140
        )
        dune = ShowRepositoryManager.retrieve_film_from_repository("Dune (2021)")
        print(ShowRepositoryViewer.display_full_film_info(dune))
