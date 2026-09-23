motorcycles = ['honda', 'yamaha', 'suzuki', 'bmw', 'kawasaki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.insert(1, 'honda')
print(motorcycles)
print(motorcycles[2])

del motorcycles[2]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

print(motorcycles)

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'A {too_expensive.title()} is too expensive for me.')