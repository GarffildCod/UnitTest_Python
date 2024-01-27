class Book:
    def __init__(self, id: str, title=None, author=None):
        self.__id: str = id
        self.__title: str = title
        self.__author: str = author

    def get_id(self) -> str:
        return self.__id

    def set_id(self, new_id: str) -> None:
        self.__id = new_id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, new_title: str) -> None:
        self.__title = new_title

    def get_author(self) -> str:
        return self.__author

    def set_author(self, new_author: str) -> None:
        self.__author = new_author