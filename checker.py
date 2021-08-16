import re
from dataclasses import dataclass


@dataclass
class CheckerInputs:

    def check_id(self, id):
        if re.fullmatch(r"^\d+$", id):
            return id
        else:
            print("Zły wzór id")
            choice = input("Wpisz poprawne id: ")
            self.check_id(id=choice)

    def check_title(self, title):
        if re.fullmatch(r"^[A-Z]{1}[a-z]+( [A-Za-z]+)*$", title):
            return title
        else:
            print("Zły wzór tytułu")
            title = input("Podaj tytuł książki: ")
            self.check_title(title=title)

    def check_author(self, author):
        if re.fullmatch(r"^[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+$", author):
            return author
        else:
            print("Zły wzór nazwy autor")
            author = input("Podaj imię i nazwisko autora: ")
            self.check_author(author=author)

    def check_genre(self, genre):
        if re.fullmatch(r"^[A-Z]{1}[a-z]+$", genre):
            return genre
        else:
            print("Zły wzór nazwy gatunek")
            genre = input("Podaj gatunek ksiażki: ")
            self.check_genre(genre=genre)

    def check_published(self, published):
        if re.fullmatch(r"^[12]{1}\d{3}-[01]{1}\d{1}-[123]{1}\d{1}$", published):
            return published
        else:
            print("Zły wzór dla formatu data")
            published = input("Podaj datę publikacji(r-m-d): ")
            self.check_published(published)
