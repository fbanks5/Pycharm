def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        c = a
        a = b
        b = c + b


for x in fibonacci(21):
    print(x)


def fibonacci2(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        c = a
        a = b
        b = c + b
    return result

print(fibonacci2(100))