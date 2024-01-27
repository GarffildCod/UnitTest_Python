from task_two.number_in_interval import number_in_interval
import unittest
from parameterized import parameterized


class NumberInIntervalTest(unittest.TestCase):
    """Разработайте и протестируйте метод number_in_interval, который проверяет, попадает ли переданное число в интервал (25;100). """

    @parameterized.expand(list(range(26, 99, 7)))
    def test_number_in_interval(self, num):
        self.assertTrue(number_in_interval(num))

    @parameterized.expand(list(range(-100, 25, 13)) + list(range(100, 1025, 13)))
    def test_number_not_in_interval(self, num):
        self.assertFalse(number_in_interval(num))