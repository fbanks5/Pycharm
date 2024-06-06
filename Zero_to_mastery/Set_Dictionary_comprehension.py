

# Set comprehension

# my_list = {char for char in 'Lebron James'}
# my_list_2 = {num for num in range(0,200)}
# my_list_3 = {num*2 for num in range(0,200)}
# my_list_4 = {num**2 for num in range(0,200) if num % 2 == 0}
#
# print(my_list)
# print(my_list_2)
# print(my_list_4)



# Dictionary comprehension

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0}
my_dict_2 = {num:num*2 for num in [1, 2, 3]}
print(my_dict_2)


