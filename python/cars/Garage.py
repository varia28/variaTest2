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

max_fuel = 0
best_fuel_car = Car
print("\n")
for i in car_data:
    car = Car(i,
              car_data[i][random.randint(0, len(car_data[i]) - 1)],
              colors[random.randint(0, len(colors) - 1)],
              random.randint(8, 16))
    car.drive(200)
    car.fuel_up()
    car.drive(100)
    if car.get_fuel() > max_fuel:
        max_fuel = car.get_fuel()
        best_fuel_car = car
    car.print_car()
    cars.append(car)

print("\n\n best car \n\n")

best_fuel_car.print_car()
