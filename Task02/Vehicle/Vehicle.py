from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def test_drive(self):
        raise NotImplementedError

    @abstractmethod
    def park(self):
        raise NotImplementedError

    def __init__(self, company: str, model: str, year_release: int, num_wheels: int, speed: float):
        self.company = company
        self.num_wheels = num_wheels
        self.speed = speed
        self.year_release = year_release
        self.model = model