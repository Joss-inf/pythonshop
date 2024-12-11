from PIL import Image
from PIL import ImageFilter
#import logger
def bluring(n:int):
    try:
        im =Image.open('KAARIS OR NOIR.jpg')
        im=im.filter(ImageFilter.GaussianBlur(n))
        file:str = 'kaaris.jpg'
        im.save(file)
        #logger.log("l'image " +file+ "a été flouté  à "+n+" %")
    except FileNotFoundError:
        print(f"Erreur : Le fichier{Image}n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
bluring(10)
