# Using a for loop

n = int(input("Enter a number: "))
ans = {}
for i in range(1, n + 1):
    ans[i] = i * i
print(ans)

# Using dictionary comprehension

n = int(input("Enter a number: "))
ans = {i : i * i for i in range(1, n + 1)}
print(ans)