from PIL import Image
from PIL import ImageFilter
def bluring(n:int):
    im =Image.open('KAARIS OR NOIR.jpg')
    im=im.filter(ImageFilter.GaussianBlur(n))
    im.save('kaaris.jpg')
bluring(10)
