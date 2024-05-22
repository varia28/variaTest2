class Car:
    def __init__(self, brand, model, color, economy):
        self._brand = brand
        self._model = model
        self._color = color
        self._economy = float(economy)
        self._fuel = int(100)
        self._mileage = int(0)

    def drive(self, distance):
        spent_fuel = distance * (self._economy / 100)
        if self._fuel < spent_fuel:
            raise Exception("not enough fuel\n")
        else:
            self._mileage = self._mileage + distance
            self._fuel = self._fuel - spent_fuel

    def distance_left(self):
        print(f"distance: {self._mileage}")
        return self._mileage

    def fuel_up(self):
        self._fuel = self._fuel + 20

    def print_car(self):
        print(f"car:   {self._brand}\nmodel: {self._model}\ncolor: {self._color}\nfuel left: {self._fuel}"
              f"\ndistance: {self._mileage}"f"\n")

    def get_fuel(self):
        return self._fuel
