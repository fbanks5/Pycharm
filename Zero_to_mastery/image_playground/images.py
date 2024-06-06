from PIL import Image, ImageFilter
img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('RGB')

filtered_img.save("rgb.png", 'png')
