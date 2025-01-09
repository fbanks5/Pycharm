word = input()
password = ''

password  = word.replace('i', '1')
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('s', '$')

password += '!'

print(f"{password}")

