from PIL import Image, ImageFilter
img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('astro_thumbnail.jpg')
img.show()


















# filtered_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# rotated = filtered_img.rotate(90)
# resize = filtered_img.resize((300, 300))

# region.save("grey.png", 'png')
# region.show()
# resize.save("grey.png", 'png')
# rotated.save("grey.png", 'png')
# filtered_img.save("rgb.png", 'png')
# resize.show()
# filtered_img.show()
# rotated.show()
