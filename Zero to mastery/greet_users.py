

# Middle Name optional, with user input.
def get_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


while True:
    print('\nPlease tell me your name.')
    print("(enter q anytime to quit)")

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    print('If no Middle name press enter')
    m_name = input('Middle name: ')
    if m_name == 'q':
        break

    formatted_name = get_full_name(f_name, l_name)
    print(f'Hi {formatted_name}!')
    break
