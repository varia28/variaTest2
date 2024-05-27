import random

from Car import Car

car_data = {
    "Volkswagen": ["Tiguan", "Golf R"],
    "Toyota": ["Camry", "Corolla", "Prius"],
    "Daimler": ["Regency", "Sovereign", "Conquest"],
    "Ford": ["Mustang", "Escape", "Focus"],
    "mahindra & mahindra": ["Scorpio", "Bolero", "Thar"],
    "BMW": ["XM", "Z4"],
    "Honda": ["Civic", "Accord", "Type R"],
    "Hyundai": ["HB20", "Sonata", "Casper"],
    "Mitsubishi ": ["Colt", "OutLander"],
    "Nissan  ": ["Leaf", "Micra", "Tiida"]
}

colors = ["red", "blue", "green", "black"]

cars = []

best_fuel_car = None
print("\n--------------")

for i in car_data:

    cars.append(
        Car(i, car_data[i][random.randint(0, len(car_data[i]) - 1)], colors[random.randint(0, len(colors) - 1)],
            random.randint(8, 16))
    )

    cars[len(cars) - 1].drive(200)
    cars[len(cars) - 1].fuel_up()
    cars[len(cars) - 1].drive(100)

    if best_fuel_car is None:
        best_fuel_car = cars[0]

    if cars[len(cars) - 1].get_fuel() > best_fuel_car.get_fuel():
        best_fuel_car = cars[len(cars) - 1]

    cars[len(cars) - 1].print_car()

print("\n\n best car \n\n--------------")

best_fuel_car.print_car()
