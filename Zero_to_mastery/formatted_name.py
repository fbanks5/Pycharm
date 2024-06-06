# Get a full name with camel case.
def get_full_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

my_name = get_full_name('frantz', 'banks')
my_mothers_name = get_full_name('Leatrice', 'Banks')
print(my_name, my_mothers_name)