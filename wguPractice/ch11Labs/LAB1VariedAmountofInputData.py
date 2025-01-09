def calculate_statistics(numbers):

    average = int(sum(numbers) / len(numbers))
    maximum = max(numbers)
    return f"{average} {maximum}"

if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    print(calculate_statistics(input_numbers))