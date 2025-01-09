names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    print(f"Name: {names[index]}")
except IndexError as e:
    print(f"Exception! {e}")

    if index < 0:
        closest_name = names[0]
    else:
        closest_name = names[-1]

    print(f"The closest name is: {closest_name}")