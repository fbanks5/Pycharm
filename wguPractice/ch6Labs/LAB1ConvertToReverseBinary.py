x = int(input())
if x > 0:
    result = ''
    while x > 0:
        result += str(x % 2)
        x = x // 2
    print(f"{result}")