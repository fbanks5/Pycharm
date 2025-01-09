def mad_libs():
    while True:
        user_input = input().split()
        word = user_input[0]
        if word == 'quit':
            break
        number = int(user_input[1])
        print(f"Eating {number} {word} a day keeps the doctor away.")

if __name__ == '__main__':
    mad_libs()