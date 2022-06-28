class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer} miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-KWh battery.')


class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a{self.battery_size}-KWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            range1= 260
        elif self.battery_size == 100:
            range1 = 315
        return range1

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


