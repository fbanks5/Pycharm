import math

frequency = float(input())
r = pow(2, 1/12)

frequency_2 = frequency * r
frequency_3 = frequency_2 * r
frequency_4 = frequency_3 * r

print(f'{frequency:.2f} Hz')
print(f'{frequency_2:.2f} Hz')
print(f'{frequency_3:.2f} Hz')
print(f'{frequency_4:.2f} Hz')