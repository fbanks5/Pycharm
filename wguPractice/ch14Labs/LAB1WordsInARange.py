# Read input
filename = input() # Name of the input file
lower_bound = input().strip() # Lower bound of the search range
upper_bound = input().strip() # Uppoer bound of the search range

with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    word = line.strip()
    if lower_bound <= word <= upper_bound:
        print(word)