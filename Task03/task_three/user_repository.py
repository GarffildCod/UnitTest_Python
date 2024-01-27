from task_three.user import User

"""Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме администраторов.
    Для этого, вам потребуется расширить класс User новым свойством, указывающим, обладает ли пользователь админскими правами.
    Протестируйте данную функцию."""


class UserRepository:
    def __init__(self):
        self.data: list[User] = list()

    def add_user(self, user: User) -> None:
        if user.is_authenticate:
            self.data.append(user)

    def log_out_user(self, user: User) -> None:
        user.is_authenticate = False
        self.data.remove(user)

    def log_out_all_users_except_admins(self) -> None:
        users_to_log_out = [user for user in self.data if not user.is_admin()]
        for user in users_to_log_out:
            self.log_out_user(user)