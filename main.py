# Cos jak filmweb:
#
# 1. Lista seriali, filmow, filmow krotkometrazowych.
# 2. Dzielo ma miec tytul, opis, srednia ocene;
# 3. Seriale maja miec sezony,
# 4. Kazdy sezon ma miec liste odcinkow
# 5. Kazdy odcinek ma miec czas trwania i tytul
# 6. Kazdy film ma miec czas trwania i tytul
# 7. Kazdy krotkometrazowy ma miec rezysera
# 8. Miec uzytkownikow na ‘filmwebie’ i zeby kazdy uzytkownik ocenil jakies dzielo
# 9. Kazdy uzytkownik ma liste “to watch”
# 10. Kazde dzielo ma kategorie
# 11. Podpowiedzi dla uzytkownikow w oparciu o oceny
#
# Docstrings + typehints + no getters or setters


from src.classes.manager_classes import FilmCreator, ShowRepositoryManager, ShowRepositoryViewer
from src.classes.user_classes import CommonUser


def main():
    # ---------- BELOW SNIPPET ILLUSTRATES THE PROCESS OF RATING A FILM ---------- #

    # FilmCreator.create_film_and_add_to_repository('Casablanca', 'A cynical expatriate American cafe owner '
    #                                                             'struggles to decide whether or not to help his '
    #                                                             'former lover and her fugitive husband escape the '
    #                                                             'Nazis in French Morocco.',
    #                                               'drama', 1958, 'michael curtiz', 102)
    # user1 = CommonUser('Rodrigo6969')
    # user1.rate_film('Casablanca (1958)', 10)
    # user2 = CommonUser('DramaQueen')
    # user2.rate_film('Casablanca (1958)', 5)
    # user3 = CommonUser('SilentBob')
    # user3.rate_film('Casablanca (1958)', 20)
    # casablanca = ShowRepositoryManager.retrieve_film_from_repository('Casablanca (1958)')
    # print(casablanca.average_rating)
    # print(user1.user_ratings)
    # print(user2.user_ratings)
    # print(user3.user_ratings)
    # ShowRepositoryViewer.view_particular_film_from_repository('Casablanca (1958)')
    pass


if __name__ == '__main__':
    main()
