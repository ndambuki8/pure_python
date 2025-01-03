from google1 import *

# my_beetle = Car('volkswagen', 'beetle', 2016)
# my_beetle.fill_tank()
# my_beetle.drive()

# my_tesla = ElectricCar('tesla', 'model s', 2016 )
# my_tesla.charge()
# my_tesla.drive()

# Make a list to hold a fleet of cars 
gas_fleet = []
electric_fleet = []

# Make 500 gas cars and 250 electric cars. 
for _ in range (500):
    car = Car('volkswagen', 'beetle', 2016)
    gas_fleet.append(car)

for _ in range(250):
    ecar = ElectricCar('tesla', 'model s', 2016)
    electric_fleet.append(ecar)

for car in gas_fleet: 
    car.fill_tank()

for ecar in electric_fleet:
    ecar.charge()

print(f"Gas cars: {len(gas_fleet)}")
print(f"Electric cars: {len(electric_fleet)}")