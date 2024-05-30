
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

def print_factorial():
    attempts = 3
    while attempts > 0:
        try:
            n = int(input("Enter a number: "))

            # Check if input is a number greater than one
            if n <= 1:
                raise ValueError

            # Function to calculate factorial
            def factorial(n):
                if n == 1:
                    return 1
                else:
                    return n * factorial(n-1)

            # Calculate and print factorial
            result = factorial(n)
            print(f"The factorial of {n} is {result}")

        except ValueError as err:
            attempts -= 1
            print(f"Error: {err}. Please enter a valid integer.")
            if attempts == 0:
                print("You have been locked out.")

print_factorial()







# Using a lambda function

# factorial = lambda n: 1 if n == 1 else n * factorial(n - 1)
# n = int(input("Enter a number: "))
# print(f"The factorial of {n} is {factorial(n)}")
