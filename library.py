from dataclasses import dataclass, field
from book import Book
from datetime import date
import json


@dataclass
class Library:
    books: list = field(default_factory=list)
    books_last_id: int = 0

    def add_book(self, title: str, author: str, genre: str, published: date):
        if len(self.books) > 0:
            last_b = self.books[-1]
            self.books_last_id = self._format_for_json(last_b)['id'] + 1
        else:
            self.books_last_id += 1
        new_book = Book(id=self.books_last_id, title=title, author=author, genre=genre, published=published)
        self.books.append(new_book)

    def print_all_books(self):
        if len(self.books) > 0:
            for book in self.books:
                print(book)
        else:
            print("Nie ma jeszcze żadanej książki w bibliotece!")

    def find_book(self, title: str):
        book_instance = None
        for book in self.books:
            if book.title == title:
                book_instance = book
                break
        return book_instance

    def remove_book(self, title: str = None, id: int = None):
        if title:
            book_instance = self.find_book(title)
            if book_instance:
                self.books.remove(book_instance)
                return True
            else:
                return False
        else:
            book_instance = None
            for book in self.books:
                if book.id == id:
                    book_instance = book
                    break
            if book_instance:
                self.books.remove(book_instance)
                return True
            else:
                return False

    @staticmethod
    def _format_for_json(b):
        if isinstance(b, Book):
            for_json = {
                "id": b.id,
                "title": b.title,
                "author": b.author,
                "genre": b.genre,
                "published": b.published.isoformat(),
                "status": b.status
            }
            return for_json

    def save_to_file(self):
        data_list = [self._format_for_json(book) for book in self.books]
        with open('saved_books.json', 'w', encoding='UTF-8') as file:
            json.dump(data_list, file)

    @staticmethod
    def _format_to_instance(d):
        if isinstance(d, dict):
            published_data = date.fromisoformat(d["published"])
            book = Book(
                id=d["id"],
                title=d["title"],
                author=d["author"],
                genre=d["genre"],
                published=published_data,
                status=d["status"]

            )
            return book

    def read_saved_data(self):
        with open("saved_books.json", 'r', encoding='UTF-8') as file:
            data_list = json.load(file)
            self.books = [self._format_to_instance(book) for book in data_list]
