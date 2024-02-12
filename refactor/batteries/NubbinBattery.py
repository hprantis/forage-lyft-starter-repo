from refactor.Battery import Battery
from refactor.utils import add_years_to_date


class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return add_years_to_date(self.last_service_date, 4) < self.current_date
