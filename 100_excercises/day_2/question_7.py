x,y = map(int,input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)


# x,y = map(int,input().split(','))
# lst = [[i*j for i in range(x)] for j in range(y)]
# print(lst)

