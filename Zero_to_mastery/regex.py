import re

# Define the regular expression pattern
pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\|,.<>\/?]).{8}$'

password_regex = re.compile(pattern)

test_passwords = ['a1!bcdef', 'abcd1234', '1234!567', '!1A2b3c4']

for password in test_passwords:
    if password_regex.fullmatch(password):
        print(f'{password} is valid')

    else:
        print(f'{password} is invalid')










# pattern = re.compile('search inside of this this text.')
# string = 'search inside of this this text. Frantz'
#
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(d)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())