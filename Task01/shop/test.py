import unittest
from .shop import Shop
from .product import Product


class ShopTest(unittest.TestCase):
    def setUp(self):
        # инициализация через setUp, а не __init__
        self.shop = Shop()
        self.kunai = Product("Кунай", 5)
        self.dart = Product("Дротик", 1)
        self.shuriken = Product("Сюрикен", 2)

    def test_add_product(self):
        # имя теста это название метода плюс префикс test_
        # assertEqual проверяет равны ли значения
        self.shop.add_product(self.kunai)
        self.shop.add_product(self.dart)
        self.assertEqual(len(self.shop.products), 2)

    def test_sort_products_by_price(self):
        self.shop.add_product(self.kunai)
        self.shop.add_product(self.dart)
        self.shop.add_product(self.shuriken)
        self.shop.sort_products_by_price()
        self.assertEqual(self.shop.products[0], self.dart)
        self.assertEqual(self.shop.products[1], self.shuriken)

    def test_get_most_expensive_product(self):
        self.shop.add_product(self.kunai)
        self.shop.add_product(self.dart)
        self.shop.add_product(self.shuriken)
        most_expensive_product = self.shop.get_most_expensive_product()
        self.assertEqual(most_expensive_product, self.kunai)

    def test_get_most_expensive_product_empty_shop(self):
        # assertIsNone проверяет равенство значения с None
        most_expensive_product = self.shop.get_most_expensive_product()
        self.assertIsNone(most_expensive_product)


if __name__ == '__main__':
    unittest.main()