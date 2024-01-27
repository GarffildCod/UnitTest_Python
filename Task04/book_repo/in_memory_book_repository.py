from book_repository import BookRepository
from book import Book


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books: dict = {
            "1": Book("1", "Book1", "Author1"),
            "2": Book("2", "Book2", "Author2")
                      }

    def find_by_id(self, id: str) -> Book:
        return self.books[id]

    def find_all(self) -> list[Book]:
        return list(self.books.values())