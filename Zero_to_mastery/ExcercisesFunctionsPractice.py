# def favorite_book(title, author, year):
#     print(f"My favorite book is {title} by {author} written in {year}")
#
#
# favorite_book('Moby Dick', 'Herman Melville', 1851)





# City and Country output
# def city_country(city, country):
#     location = f" {city} {country}"
#     return location
#
#
# my_location = city_country("Jacksonville", "France")
# print(my_location)

def make_album(artist, title, songs='none'):
    album_info = {'artist': artist, 'title': title, 'songs': songs}
    return album_info


my_album_1 = make_album('The Tempations', 'Silent Night', 6)
my_album_2 = make_album('Whitney Houston', 'Whitney Houston', 12)

print(my_album_1)
print(my_album_2)
