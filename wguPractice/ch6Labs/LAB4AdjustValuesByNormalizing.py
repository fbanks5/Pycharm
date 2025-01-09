# Read the number of values
num_values = int(input("Enter the number of values: "))

# Read the floating-point values into a list
values = []
for _ in range(num_values):
    value = float(input("Enter a value: "))
    values.append(value)

# Find the largest value
max_value = max(values)

# Normalize the values by dividing each by the largest value
for i in range(num_values):
    values[i] = values[i] / max_value

# Output each normalized value with two decimal places
for value in values:
    print(f'{value:.2f}')