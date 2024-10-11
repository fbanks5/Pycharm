highway_number = int(input())

if highway_number % 100 == 0:
    print(f'{highway_number} is not a valid interstate highway number.')
elif 1 <= highway_number < 100:
    if highway_number % 2 == 0:
        print(f'{highway_number} is primary, going east/west.')
    else:
        print(f'{highway_number} is primary, going north/south.')
elif 100 <= highway_number < 1000:
    primary_highway = highway_number % 100
    if primary_highway == 0:
        print(f'{highway_number} is not a valid interstate highway number.')
    else:
        if highway_number % 2 == 0:
            print(f'{highway_number} is auxiliary, serving I-{primary_highway}, going east/west.')
        else:
            print(f'{highway_number} is auxiliary, serving I-{primary_highway}, going north/south.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')