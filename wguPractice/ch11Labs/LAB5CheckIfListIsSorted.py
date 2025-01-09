def in_order(numbers):
    # Iterate through the list and compare each element to the next
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True
