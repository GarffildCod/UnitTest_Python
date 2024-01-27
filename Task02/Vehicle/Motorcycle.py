from .Vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, year_release):
        super().__init__(company, model, year_release, 2, 0)

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0