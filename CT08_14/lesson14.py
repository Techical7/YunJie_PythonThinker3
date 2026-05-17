class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def show_details(self):
        print(f"{self.make} {self.model} - ${self.price}")

    def start_engine(self):
        print(f"{self.make} {self.model} engine started")

bmw = Car("BMW", "Z4", 500000)
toyota = Car("Toyota", "Corolla", 180000)
kia = Car("Kia", "Cerato", 165000)

showroom = []
showroom.append(bmw)
showroom.append(toyota)
showroom.append(kia)

for car in showroom:
    car.show_details()