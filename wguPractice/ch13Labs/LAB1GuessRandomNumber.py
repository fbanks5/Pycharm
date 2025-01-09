import random

def number_guess(num):
    random_number = random.randint(1, 100)

    if num == random_number:
        print(f"{num} is correct!")
    elif num < random_number:
        print(f"{num} is too low. Random number was {random_number}.")
    else:
        print(f"{num} is too high. Random number was {random_number}.")

if __name__ == '__main__':
    random.seed(900)

    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)