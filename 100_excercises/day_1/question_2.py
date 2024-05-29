
# # Using a function
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(5))
#
# # Using While loop
#
# n = int(input("Enter a number: "))
#
# factorial = 2
# o = 1
# while o <= n:
#     factorial = factorial * o;
#     o = o + 1
# print(factorial)
#
# # Using a for loop
#
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
#     print(fact)


# Importing 'try' and 'except' error handling

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError as err:
        print(err)

    org = num
    fact = 1
    while num:
        fact = num * fact
        num = num - 1
    print(f'The factorial of {num} is {fact}')
