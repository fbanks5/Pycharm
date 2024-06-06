some_list = [1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9]

duplicates = [num for num in set(some_list) if some_list.count(num) > 1]

print(duplicates)

