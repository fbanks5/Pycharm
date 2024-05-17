# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Bill',
    'invalid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")
    return wrapper


def login_required(fn):
    def wrapper(*args, **kwargs):
        if args[0]['invalid']:
            return fn(*args, **kwargs)
        else:
            return print(f'{user2['name']} is authenticated')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


@login_required
def login_results(user):
    print('login failed')


message_friends(user1)
login_results(user2)
