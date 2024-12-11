
def gray_filter(img):
    """
    Applique un filtre de conversion en niveaux de gris à une image.

    Cette fonction convertit l'image donnée en mode L (Luminance) pour obtenir une version en noir et blanc de l'image.

    Args:
        img (PIL.Image.Image): L'image à convertir, sous forme d'objet Image de la bibliothèque Pillow.

    Returns:
        PIL.Image.Image: L'image convertie en niveaux de gris.

    Raises:
        FileNotFoundError: Si le fichier d'image spécifié n'a pas été trouvé.
        Exception: Si une erreur quelconque se produit pendant le traitement de l'image.
    """
    try:
        # Convertir l'image en niveaux de gris
        return img.convert("L")
    except FileNotFoundError:
        print(f"""Erreur : Le fichier {img} n'a pas été trouvé.""")
    except Exception as e:
        print(f"""Une erreur s'est produite : {e}""")

