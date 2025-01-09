def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())
    swapped_values = swap_values(user_val1, user_val2, user_val3, user_val4)
    print(f"{swapped_values[0]} {swapped_values[1]} {swapped_values[2]} {swapped_values[3]}")