class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make,model,year)
        self.body_syle = body_style


class ElectricalCar(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style)
        self.battery_capcacity = battery_capacity

    def charger(self):
        print("Charging the electric car.")


tesla = ElectricalCar("Tesla", "Cybertruck",2023, "SUV", "400Mhw")
tesla.display_info()
print(tesla.battery_capcacity)
print(tesla.body_syle)
tesla.charger()