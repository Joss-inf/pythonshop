from PIL import Image


def resizedImg(htr:int,lgr:int) ->None: #hauteur , largeur

    
    try:

        file = 'profil-img.png'
        folder = 'sortie/'
        img = Image.open(file)
        resized_image = img.resize((htr, lgr))
        resized_image.save(folder+f'resize{htr,lgr}'+file)

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
rotateImg(60)