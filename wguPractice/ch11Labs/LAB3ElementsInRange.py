# Get a list of numbers from the user
input_numbers = list(map(int, input().split()))

lower_bound, upper_bound = map(int, input().split())

for num in input_numbers:
    if lower_bound <= num <= upper_bound:
        print(num, end=" ")

