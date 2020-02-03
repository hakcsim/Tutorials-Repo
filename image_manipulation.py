import os, glob
from PIL import Image, ImageFilter

image = Image.open('puppy.jpg')

# rotate
image.rotate(90).show()

# convert to gray scale
image.convert(mode='L').show()

image.filter(ImageFilter.GaussianBlur(15)).show()

os.chdir('test_files')

for file in os.listdir():
    if file.endswith('.jpg'):
        print(file)

if not os.path.exists('png_files'):
    os.mkdir('png_files')

size_128 = (128, 128)
size_256 = (256, 256)

for file in glob.glob('*.jpg'):
    print(file)
    fname, extname = os.path.splitext(file)
    image = Image.open(file)

    # resize
    image.thumbnail(size_128)
    image.save(f'png_files/{fname}_128.png')
    image.thumbnail(size_256)
    image.save(f'png_files/{fname}_256.png')


