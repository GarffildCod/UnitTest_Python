import unittest

from task_three.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Zhenya", "test")

    def tearDown(self):
        del self.user

    def test_authentication_pass(self):
        self.user.authenticate("Zhenya", "test")
        self.assertTrue(self.user.is_authenticate)

    def test_authentication_failed(self):
        self.user.authenticate("Zhenya", "")
        self.assertFalse(self.user.is_authenticate)