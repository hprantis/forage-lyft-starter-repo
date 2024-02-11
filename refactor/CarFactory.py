from refactor.Car import Car
from refactor.engines import SternmanEngine
from refactor.engines import CapuletEngine
from refactor.engines import WilloughbyEngine
from refactor.batteries import NubbinBattery
from refactor.batteries import SpindlerBattery


class CarFactory(Car):

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine.CapuletEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery.SpindlerBattery(last_service_date, current_date)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine.WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery.SpindlerBattery(last_service_date, current_date)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.engine = SternmanEngine.SternmanEngine(warning_light_on)
        self.battery = SpindlerBattery.SpindlerBattery(last_service_date, current_date)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine.WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery.NubbinBattery(last_service_date, current_date)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine.CapuletEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery.NubbinBattery(last_service_date, current_date)










