# Decorator


# def my_decorator(func):
#     def wrapper():
#         print('Above')
#         func()
#         print('Below')
#     return wrapper
#
# @my_decorator
# def hello():
#     print("Hello World!")
#
# @my_decorator
# def bye():
#     print("Goodbye!")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Above")
        func(*args, **kwargs)
        print("Below")
    return wrapper

@my_decorator
def hello(greeting, salutation):
    print(greeting, salutation)


hello("Hello", "Goodbye")