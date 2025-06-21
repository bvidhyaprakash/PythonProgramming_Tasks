class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + 50 * days

class Bike(Vehicle):
    def calculate_rental(self, days):
        return self.rental_rate * days


class Truck(Vehicle):
    def calculate_rental(self, days):
        return super().calculate_rental(days) + 100 * days


print("\nVehicle rental calculation")
print("---------------------------")
Vehicle_1 = Car("Velkswagon Vento", 3000)
Vehicle_2 = Bike("RE 500", 1500)
Vehicle_3 = Truck("Volvo Truck", 4000)

print(f"{Vehicle_1.model} rent for 2 days : {Vehicle_1.calculate_rental(2)}")
print(f"{Vehicle_2.model} rent for 5 days : {Vehicle_2.calculate_rental(5)}")
print(f"{Vehicle_3.model} rent for 3 days : {Vehicle_3.calculate_rental(3)}")