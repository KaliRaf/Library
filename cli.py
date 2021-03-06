from dataclasses import dataclass
from datetime import date
from library import Library
from checker import CheckerInputs


@dataclass
class CLI:
    libr: Library = Library()

    @staticmethod
    def print_menu():
        print("\n1. Pokaż wszystie książki.")
        print("2. Dodaj książkę. ")
        print("3. Usuń książkę. ")
        print("4. Wyszukaj książkę. ")
        print("5. Zakończ program. ")

    def switch(self):
        switch = {
            "1": self.libr.print_all_books,
            "2": self._data_for_book,
            "3": self._data_for_delete,
            "4": self._data_for_find,
            "5": self._end
        }
        try:
            answer = input("Jakiego wyboru dokonujesz? \n")
            switch[answer]()
        except KeyError:
            print("Zły wybór, wybierz jeszcze raz:")
            self.switch()

    def load_archived_data(self):
        try:
            self.libr.read_saved_data()
        except FileNotFoundError:
            print("Import pliku się nie powiódł...")

    def _data_for_delete(self):
        check_it = CheckerInputs()
        choice = input("Jeśli chcesz usunąć książkę wpisz jej tytuł lub id: ")
        if choice.isdigit() and self.libr.find_book(choice) is None:
            id_str = check_it.check_id(choice)
            id = int(id_str)
            if self.libr.find_book(id=id):
                self.libr.remove_book(id=id)
                print(f"Usunięto książkę z nr id {id_str}")
            else:
                print("Nie można usunąć książki,\nponieważ nie istnieje.")
        else:
            title = check_it.check_title(choice)
            if self.libr.find_book(title=title):
                self.libr.remove_book(title=title)
                print(f"Usunięto książkę o tytule {title}")
            else:
                print("Nie można usunąć książki,\nponieważ nie istnieje.")

    def _data_for_book(self):
        check_it = CheckerInputs()
        title = input("Podaj tytuł książki: ")
        check_it.check_title(title)

        author = input("Podaj imię i nazwisko autora: ")
        check_it.check_author(author)

        genre = input("Podaj gatunek ksiażki: ")
        check_it.check_genre(genre)

        published = input("Podaj datę publikacji(r-m-d): ")
        published_y = check_it.check_published(published)
        published_x = date.fromisoformat(published_y)

        self.libr.add_book(title, author, genre, published=published_x)

    def _data_for_find(self):
        check_it = CheckerInputs()
        find = input("Podaj tytuł lub id książki: ")
        if find.isdigit():
            find1 = check_it.check_id(find)
            finded = self.libr.find_book(id=find1)
        else:
            find1 = check_it.check_title(find)
            finded = self.libr.find_book(title=find1)

        if finded is None:
            print("Nie znaleziono takiej książki!")
        else:
            print(finded)
            print(finded.get_more_information())

    def _end(self):
        self.libr.save_to_file()
        quit()
