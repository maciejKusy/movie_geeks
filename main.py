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

from src.classes.show_classes import Show
from src.classes.manager_classes import RecordManager


def main():
    manager = RecordManager()
    manager.create_film_and_add_to_repository()



if __name__ == '__main__':
    main()
