quarters = int(input())
dimes = int(input())
nickels = int(input())
pennies = int(input())

total_cents = (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
dollars = total_cents / 100

print(f"Amount: ${dollars:.2f}")