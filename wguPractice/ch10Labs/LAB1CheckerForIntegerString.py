def format_name(name):
    name_parts = name.split()
    if len(name_parts) == 3:
        first_name, middle_name, last_name = name_parts
        return f"{last_name}, {first_name[0]}.{middle_name[0]}."
    elif len(name_parts) == 2:
        first_name, last_name = name_parts
        return f"{last_name}, {first_name[0]}."
    else:
        return "Invalid input"

if __name__ == '__main__':
    name = input()
    print(format_name(name))