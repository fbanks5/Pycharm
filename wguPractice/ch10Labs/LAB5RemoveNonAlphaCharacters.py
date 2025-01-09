def remove_non_alpha(input_string):
    return ''.join(filter(str.isalpha, input_string))

if __name__ == '__main__':
    input_string = input()
    print(remove_non_alpha(input_string))