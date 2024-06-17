import Pokedex
import sys
import os
from PIL import Image

# Using sys module grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]



# Check if new/ exists, if not create folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)



# Loop through Pokedex
for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')




# Convert images to PNG

# Save them to the new folder