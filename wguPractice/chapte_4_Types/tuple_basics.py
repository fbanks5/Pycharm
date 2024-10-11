from collections import namedtuple

Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8) # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5) # Use the named tuple to describe a different car

print(chevy_impala)
print(chevy_blazer)
print('Chevy Blazer make: ', chevy_blazer.make)
print(chevy_impala.model)

// compute the sum of the prices of the two cars
