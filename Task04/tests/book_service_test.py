from book_repo.book import Book
from book_repo.book_service import BookService
from book_repo.book_repository import BookRepository
from unittest import TestCase, main, mock


class BookServiceTest(TestCase):

    def setUp(self):
        # Создание мок-объекта Mock, который имитирует поведение объекта BookRepository.
        # Он используется в качестве замены реального объекта BookRepository при создании экземпляра класса BookService.
        self.mock_book_repository: mock = mock.Mock(spec=BookRepository)
        # сам book_service продолжает работать без изменений
        self.book_service: BookService = BookService(self.mock_book_repository)

    def tearDown(self):
        del self.mock_book_repository
        del self.book_service

    def test_find_book_by_id(self):
        book_id: str = "01"
        test_book: Book = Book("01", "Book01", "Author01")

        # закидываем тестовую книгу в мок-репозиторий
        self.mock_book_repository.find_by_id.return_value = test_book

        # берем книгу из мок-репозитория по индексу
        book_from_repo: Book = self.book_service.find_book_by_id(book_id)

        self.assertEqual(test_book.get_id(), book_from_repo.get_id())
        self.assertEqual(test_book.get_title(), book_from_repo.get_title())
        self.assertEqual(test_book.get_author(), book_from_repo.get_author())

        # Проверка, что метод find_by_id вызывается один раз с заданным идентификатором.
        self.mock_book_repository.find_by_id.assert_called_once_with(book_id)

    def test_find_all_books(self):
        test_books: list[Book] = [Book("01", "Book01", "Author01"),
                                  Book("02", "Book02", "Author02"),
                                  Book("03", "Book03", "Author03")]

        # закидываем книги в мок-репозиторий
        self.mock_book_repository.find_all.return_value = test_books

        # вызвали все книги из репозитория через интерфейс
        actual_books: list[Book] = self.book_service.find_all_books()

        # циклом проверяем каждую книгу
        for test_book, actual_book in zip(test_books, actual_books):
            self.assertEqual(test_book.get_id(), actual_book.get_id())
            self.assertEqual(test_book.get_title(), actual_book.get_title())
            self.assertEqual(test_book.get_author(), actual_book.get_author())

        # Проверка, что метод вызывается один раз
        self.mock_book_repository.find_all.assert_called_once_with()


if __name__ == '__main__':
    main()