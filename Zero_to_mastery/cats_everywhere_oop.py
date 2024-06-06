class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('John', 100)
cat2 = Cat('Tom', 50)
cat3 = Cat('Butch', 5)


def oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {oldest_cat(cat1.age, cat1.age, cat1.age)} years old')
