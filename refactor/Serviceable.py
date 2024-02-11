from refactor.Car import Car


class Serviceable(Car):

    def needs_service(self):
        return self.engine.needs_service(), self.battery.needs_service()
