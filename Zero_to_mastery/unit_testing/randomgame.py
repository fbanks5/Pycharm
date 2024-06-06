import sys

sys.argv
import random

#num_list = random.randint(int(sys.argv[1]), int(sys.argv[2]))
# random_num = random.choice(num_list)

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You guessed the right number!')
            return True
    else:
        print('remember, between 1 and 10')
        return False

if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number between 1 and 10: '))
            if (run_guess(guess, answer)):
                break
            if 0 < guess < 11:
                if guess == answer:
                    print('You guessed the right number!')
                    break
            else:
                print('remember, between 1 and 100')
        except ValueError:
            print('That\'s not a number!')
            continue


