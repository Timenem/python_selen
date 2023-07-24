class Car():
    wheels = 'four'
    doors = 4
    working_engine = False

    def __init__(self, brand='', model='', fuel_consumption=7):
        self.brand = brand
        self.model = model
        self.fuel_used = 0
        self.fuel_consumption = fuel_consumption

    def __set_engine(self, value: bool):
        self.working_engine = value
        # return self.working_engine

    def start_engine(self):
        self.__set_engine(True)
        print("Engine has started")

    def stop_engine(self):
        self.__set_engine(False)
        print("Engine has stopped")

    def drive(self, distance: int, ):
        if self.working_engine:
            one_liter_per_kilometer = self.fuel_consumption / 100
            self.fuel_used = round(one_liter_per_kilometer * distance, 2)
            print(f"Currently driven {distance} km, total fuel used - {self.fuel_used} l")
        else:
            print("Start the car before driving!")


my_car = Car('', '')
some_car1 = Car(brand='Ford', model='Mustang')
some_car2 = Car(brand='', model='Camaro')
some_car1.start_engine()
some_car2.start_engine()


class ElectricCar(Car):
    def __init__(self, battery_capacity: int, **kwargs):
        self.battery_capacity = battery_capacity
        super().__init__(**kwargs)

    def __set_engine(self, value: bool):
        self.working_engine = value

    def start_engine(self):
        self.__set_engine(value=True)
        print('Electric motor has started')

    def stop_engine(self):
        self.__set_engine(value=False)
        print('Electric motor has stopped')

    def drive(self, distance: int):
        if self.working_engine:
            print(f"Currently driven {distance} km on electric motor")
        else:
            print("Start the car before driving!")


my_electric_car = ElectricCar(battery_capacity=100, model='Model 3', brand='Tesla')
my_electric_car.start_engine()
my_electric_car2 = ElectricCar(battery_capacity=60, model='Prius', brand='Toyota')
my_electric_car2.start_engine()
my_electric_car2.stop_engine()
