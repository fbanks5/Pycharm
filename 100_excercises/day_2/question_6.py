import math as m

C, H = 50, 30


def calculation(D):
    D = int(D)
    return str(int(m.sqrt((2 * C * D) / H)))

D = input().split(',')
D = list(map(calculation, D))
print(', '.join(map(str, D)))


