from car import Car
from electric_car import ElectricCar as EC

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_mustang.read_odometer()
my_mustang.update_odometer(100)
my_mustang.read_odometer()
my_mustang.increment_odometer(23)
my_mustang.read_odometer()

print("---")

my_leaf = EC('nissan', 'leaf', 2024, 65)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
