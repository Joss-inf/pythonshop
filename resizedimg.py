from PIL import Image


def resizedImg(facteur:int) ->None: #hauteur , largeur
    """permet de redimensionner l'image en fonction du facteur donner en paramètres
    facteur : facteur de scaling par lequel on va multiplier la longueur et la hauteur de l'image
    return : l'image modifier en fonction du facteur
    """
    
    try:
        lgr, htr = img.size * facteur
        file = 'profil-img.png'
        img = Image.open(file)
        return img.resize((lgr, htr))

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


