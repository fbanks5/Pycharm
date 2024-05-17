
from functools import reduce
# lambda param: action(param)

my_list = [1, 2, 3, 4, 5]
my_list_two = [6, 7, 8, 9, 10]
my_list_three = [11, 12, 13, 14, 15]


# def multiply_list(number):
#     return number * 2


# def only_odd(number):
#     return number % 2 != 0


# def accumulator(acc, item):
#     print(acc, item)
#     return acc * item


print(list(map(lambda number: number*2, my_list)))
print(list(filter(lambda number: number % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc * item, my_list))

# print(reduce(accumulator, my_list, 2))
# print(list(zip(my_list, my_list_two, my_list_three)))  # zip()
# print(list(map(multiply_list, my_list_two)))

# print(my_list)
