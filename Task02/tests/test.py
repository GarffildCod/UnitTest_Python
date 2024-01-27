import unittest
from parameterized import parameterized

from dz2_framework.Vehicle.Vehicle import Vehicle
from dz2_framework.Vehicle.Car import Car
from dz2_framework.Vehicle.Motorcycle import Motorcycle


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """Метод создает новый экземпляр для каждого теста"""
        self.car = Car("Toyota", "Trueno", 1995)
        self.moto = Motorcycle("Honda", "cbr600", 2010)

    def tearDown(self):
        """Метод удаляет экземпляр по завершению теста"""
        del self.car
        del self.moto

    def test_Car_is_Vehicle(self):
        """Проверить, что экземпляр объекта Car также является экземпляром транспортного средства."""
        # вариант1
        self.assertTrue(isinstance(self.car, Vehicle))
        # вариант2
        self.assertIsInstance(self.car, Vehicle)

    @parameterized.expand([  # тест с вводом параметров
        ["BMW", "320", 1987],  # список со списком значений, которые будут передаваться в тест циклом
        ["Subaru", "Legacy", 2015]
    ])
    def test_Car_is_created_with_four_wheels(self, company, model, year):
        """Проверить, что объект Car создается с 4-мя колесами."""
        car = Car(company, model, year)
        self.assertEqual(car.num_wheels, 4)
        del car

    def test_Motorcycle_is_created_with_two_wheels(self):
        """Проверить, что объект Motorcycle создается с 2-мя колесами."""
        self.assertEqual(self.moto.num_wheels, 2)

    def test_Car_speed_in_test_mode(self):
        """Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive())."""
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_Motorcycle_speed_in_test_mode(self):
        """Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive())."""
        self.moto.test_drive()
        self.assertEqual(self.moto.speed, 75)

    def test_Car_stopped_in_park_mode(self):
        """Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0)."""
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_Motorcycle_stopped_in_park_mode(self):
        """Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0)"""
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto.speed, 0)


if __name__ == '__main__':
    unittest.main()