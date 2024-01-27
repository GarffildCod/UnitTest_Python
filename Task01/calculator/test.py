import unittest2 as unittest
from .discount_calculator import Calculator, ArithmeticException


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculateDiscount_validInput(self):
        # сравнивает два значения
        self.assertEqual(self.calculator.calculate_discount(100, 10), 90)
        self.assertEqual(self.calculator.calculate_discount(200, 20), 160)
        self.assertEqual(self.calculator.calculate_discount(500, 25), 375)

    def test_calculateDiscount_invalidInput(self):
        """Метод `assertRaises` используется для проверки,
        что определённое исключение будет вызвано при выполнении определенного блока кода.
        Если исключение указанного типа было вызвано, тест проходит успешно.
        Если исключение не было вызвано или вызвано исключение другого типа,
        тест не пройдёт и будет вызвано исключение `AssertionError`."""
        self.assertRaises(ArithmeticException, self.calculator.calculate_discount, -100, 10)
        self.assertRaises(ArithmeticException, self.calculator.calculate_discount, 100, -10)
        self.assertRaises(ArithmeticException, self.calculator.calculate_discount, 100, 110)


if __name__ == '__main__':
    unittest.main()