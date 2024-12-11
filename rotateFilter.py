def rotateImg(img, dgr: int):
    """
    Effectue une rotation d'une image selon un nombre de degrés spécifié.

    Cette fonction prend une image et un angle de rotation en degrés, et retourne l'image pivotée. 
    L'angle de rotation doit être compris entre 0 et 360 degrés. Si l'angle est en dehors de cette plage, 
    un message d'erreur est affiché.

    Args:
        img (PIL.Image.Image): L'image à faire pivoter, sous forme d'objet Image de la bibliothèque Pillow.
        dgr (int): L'angle de rotation en degrés (doit être entre 0 et 360).

    Returns:
        PIL.Image.Image: L'image après rotation.

    Raises:
        FileNotFoundError: Si le fichier d'image spécifié n'a pas été trouvé.
        Exception: Si une erreur quelconque se produit pendant le traitement de l'image.
    """
    # Vérification que l'angle est dans la plage valide
    if dgr < 0 or dgr > 360:
        print("Erreur : L'angle doit être compris entre 0 et 360 degrés.")
        return

    try:
        # Appliquer la rotation à l'image
        return img.rotate(dgr)
    except FileNotFoundError:
        # Gérer l'erreur si l'image n'est pas trouvée
        print(f"Erreur : Le fichier {img} n'a pas été trouvé.")
    except Exception as e:
        # Gérer toute autre exception
        print(f"Une erreur s'est produite : {e}")
