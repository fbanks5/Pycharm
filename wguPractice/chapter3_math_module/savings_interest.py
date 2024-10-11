import math

base = float(input('Enter the initial amoutn of money in the account:'))

rate = float(input('Enter the annual interest rate: '))

years = int(input('Enter years that pass: '))

total = base * math.pow(1 + (rate / 100), years)

print(f'Savings after {years} years: is ${total:.2f}.')