# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    print(f"{driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}")
    print(f"{driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}")
    print(f"{driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}")