class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('John', 100)
cat2 = Cat('Tom', 200)
cat3 = Cat('Butch', 5000)


def oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')
