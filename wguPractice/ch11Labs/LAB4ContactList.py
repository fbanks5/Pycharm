contact_input = input().split()

contact = {}
for pair in contact_input:
    name, phone = pair.split(',')
    contact[name] = phone

search_name = input().strip()

print(contact[search_name])