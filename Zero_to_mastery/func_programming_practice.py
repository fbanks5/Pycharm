# my_list = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
# my_list_2 = ['cyan', 'magenta', 'white']
# def _sort(my_list):
#     return sorted(my_list)

from functools import reduce

my_list = [1, 2, 3, 4, 5]
my_list_two = [6, 7, 8, 9, 10]
my_list_three = [11, 12, 13, 14, 15]


def multiply_list(number):
    return number * 2


def only_odd(number):
    return number % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc * item


print(reduce(accumulator, my_list, 2))
print(list(zip(my_list, my_list_two, my_list_three)))  # zip()
print(list(map(multiply_list, my_list_two)))
print(list(filter(only_odd, my_list)))
print(my_list)
