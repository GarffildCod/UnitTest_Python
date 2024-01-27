from book_repo.book_repository import BookRepository
from book_repo.book import Book


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository: BookRepository = book_repository

    def find_book_by_id(self, id: str) -> Book:
        return self.book_repository.find_by_id(id)

    def find_all_books(self) -> list[Book]:
        return self.book_repository.find_all()