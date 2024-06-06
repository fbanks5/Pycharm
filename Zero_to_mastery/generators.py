# Generators

# def generator_function(num):
#     for i in range(num):
#         yield i*2
#
# # for i in generator_function(1000):
# #     print(i)
#
# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

class MyGen():
    counter = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.counter < self.last:
            num = MyGen.counter
            MyGen.counter += 1
            return num
        raise StopIteration

gen = MyGen(1, 100)
for i in gen:
    print(i)