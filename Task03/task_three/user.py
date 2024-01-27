class User:
    def __init__(self, username: str, password: str, is_admin=False):
        self.username = username
        self.password = password
        self.__is_admin = is_admin
        self.is_authenticate = False

    def authenticate(self, username: str, password: str) -> None:
        if username == self.username and password == self.password:
            self.is_authenticate = True

    def is_admin(self) -> bool:
        return self.__is_admin