def filter_and_sort_list(numbers):
    non_negative_numbers = [num for num in numbers if num >= 0]
    non_negative_numbers.sort()
    return non_negative_numbers

if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    sorted_non_negative_numbers = filter_and_sort_list(input_numbers)
    print(" ".join(map(str, sorted_non_negative_numbers)), end=" ")