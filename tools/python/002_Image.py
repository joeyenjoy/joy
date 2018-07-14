#RESIZE

from PIL import Image

image_path = ''
output_path = ''
width = 229
height = 229
image = Image.open(image_path)
out = image.resize((width, height))

out.save(output_path, 'jpg')
