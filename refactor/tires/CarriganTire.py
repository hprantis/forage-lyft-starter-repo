from refactor.tires.Tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        return max(self.tire_wear_array) >= 0.9
