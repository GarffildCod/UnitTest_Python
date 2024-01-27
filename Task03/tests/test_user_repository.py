import unittest

from task_three.user import User
from task_three.user_repository import UserRepository


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()
        self.user = User("Zhenya", "test")

    def tearDown(self):
        del self.user
        del self.user_repo

    def test_add_authorized_user_to_repository(self):
        self.user.authenticate("Zhenya", "test")
        self.user_repo.add_user(self.user)
        self.assertTrue(self.user in self.user_repo.data)

    def test_add_not_authorized_user_to_repository(self):
        self.user.authenticate("Zhenya", "")
        self.user_repo.add_user(self.user)
        self.assertFalse(self.user in self.user_repo.data)

    def test_log_out_user(self):
        self.user.authenticate("Zhenya", "test")
        self.user_repo.add_user(self.user)
        self.user_repo.log_out_user(self.user)
        self.assertFalse(self.user in self.user_repo.data)

    def test_log_out_all_users_except_admins(self):
        # Создаем список псевдо-пользователей
        users = [
            User("User1", "pass1"),
            User("User2", "pass2"),
            User("User3", "pass3"),
            User("User4", "pass4"),
            User("User5", "pass5")
        ]

        # авторизуем каждого через цикл
        for user in users:
            user.authenticate(user.username, user.password)
            self.user_repo.add_user(user)

        # Создаем псевдо-админов
        admins = [
            User("Admin1", "pas1", True),
            User("Admin2", "pas2", True),
            User("Admin3", "pas3", True),
        ]

        # авторизуем каждого
        for admin in admins:
            admin.authenticate(admin.username, admin.password)
            self.user_repo.add_user(admin)

        self.user_repo.log_out_all_users_except_admins()

        # длина списка находящихся в системе должна быть равна числу оставшихся авторизированных админов
        self.assertEqual(len(self.user_repo.data), 3)