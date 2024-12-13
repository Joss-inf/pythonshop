import logger



def resizedImg(img, facteur: int):
    """
    Redimensionne l'image en fonction du facteur donné en paramètres.
    
    Args:
        img (Image): L'image à redimensionner.
        facteur (int): Le facteur de mise à l'échelle (par exemple, 2 pour doubler la taille).
    
    Returns:
        Image: L'image redimensionnée en fonction du facteur.
    """
    try:
        # Obtenir les dimensions actuelles de l'image
        lgr, htr = img.size

        # Calculer les nouvelles dimensions après application du facteur
        lgr, htr = int(lgr * facteur), int(htr * facteur)

        # Appliquer le redimensionnement
        resized_image = img.resize((lgr, htr))
        # Log ou message pour indiquer le changement de taille
        logger.log(f"Image redimensionnée avec un facteur de : {facteur}")
        return resized_image

    except Exception as e:
        print(f"Une erreur s'est produite lors du redimensionnement de l'image : {e}")
        return None



