from dataclasses import dataclass
from datetime import date


@dataclass
class Book:
    id: int
    title: str
    author: str
    genre: str
    published: date
    status: str = 'Available'

    def __str__(self):
        return f'{self.id}: {self.title} by {self.author}'

    def get_more_information(self):
        return f"Gatunek: {self.genre}\nData publikacji: {self.published}\nStatus: {self.status}"
