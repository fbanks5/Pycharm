def int_to_reverse_binary(integer_value):
    if integer_value > 0:
        result = ''
        while integer_value > 0:
            result = result + str(integer_value % 2)
            integer_value = integer_value // 2
        return result

def string_reverse(string_value):
    return string_value[::-1]

if __name__ == '__main__':
    integer_value = int(input())
    reverse_binary = int_to_reverse_binary(integer_value)
    binary_string = string_reverse(reverse_binary)
    print(binary_string)