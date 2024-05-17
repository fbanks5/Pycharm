from collections import defaultdict, Counter, OrderedDict


# li = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# sentence = 'Test sentence for python'
# dictionary = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2, 'c': 3, 'd': 4})
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2


# print(Counter(li))
# print(Counter(sentence))
# print(dictionary['b'])
print(d2 == d)