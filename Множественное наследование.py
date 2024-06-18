class Vehicle:
    def __init__(self):
        self.vehicle_type = 'none'

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return self.horse_powers()

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 2000000
        self.vehicle_type = 'Coupe'
        self.horse_powers = 150

nissan = Nissan()

print(f'Тип машины: {nissan.vehicle_type}')
print(f'Цена: {nissan.price}')
print(f'Лошадиные силы: {nissan.horse_powers}')
