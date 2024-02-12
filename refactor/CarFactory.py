from refactor.Car import Car
from refactor.engines import SternmanEngine
from refactor.engines import CapuletEngine
from refactor.engines import WilloughbyEngine
from refactor.batteries import NubbinBattery
from refactor.batteries import SpindlerBattery


class CarFactory(Car):
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine.CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery.SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery.SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine.SternmanEngine(warning_light_on)
        battery = SpindlerBattery.SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery.NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine.CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery.NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car











