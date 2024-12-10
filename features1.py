from PIL import Image
from PIL import ImageFilter
im =Image.open('KAARIS OR NOIR.jpg')
im.show()              
pixels=im.load()
im = im.filter(ImageFilter.GaussianBlur(8))
ima = im.save("kaaris.jpg")