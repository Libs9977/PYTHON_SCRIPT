# Importing Required Modules
from rembg import remove
from PIL import Image

# Store path of the image in the variable input_path
input_path = 'test1.JPG'

# Store path of the output image in the variable output_path
output_path = 'test1Processed.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

