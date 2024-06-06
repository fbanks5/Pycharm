class Restaurant:
    def __init__(self, name, cuisine_type, number_served):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'The restaurant name is {self.name} and the cuisine type is {self.cuisine_type} and the number served is'
              f' {self.number_served}')
        return 'done'

    def open_restaurant(self):
        print(f'{self.name} is open!')
        return 'done'

    def increment_number_served(self):
        input('How many customer were served?\n')
        if Restaurant.number_served >= 0:
            print(f' The number of customers served is {Restaurant.number_served}.')



first_restaurant = Restaurant('The Italian Spot', 'Italian', 100)
second_restaurant = Restaurant('Burger Joint', 'American', 50)
third_restaurant = Restaurant('A taste of Greece', 'Greek and Mediterranean', 1000)


print(first_restaurant.describe_restaurant())




# class User:
#     def __init__(self, first_name, last_name, age, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender
#
#     def describe_user(self):
#         print(f'User info:\n{self.first_name}\n{self.last_name}\n{self.age}\n{self.gender}')
#         return 'done'
#
#     def greet_user(self):
#         print(f'Hello, {self.first_name} {self.last_name} you are {self.age} years old and are {self.gender}.')
#         return 'done'
#
#
# first_user = User('John', 'Doe', 30, 'Male')
# second_user = User('Jane', 'Doe', 40, 'Female')
# third_user = User('Bill', 'Johnson', 25, 'Male')
# fourth_user = User('Thomas', 'Cunningham', 62, 'Zebra')

# print(first_user.describe_user())
# print(first_user.greet_user())
# print(second_user.describe_user())
# print(second_user.greet_user())
# print(third_user.describe_user())
# print(third_user.greet_user())
# print(fourth_user.describe_user())
# print(fourth_user.greet_user())

