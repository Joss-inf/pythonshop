from PIL import ImageDraw, ImageFont
def textFilter(image, text):
    text = str(text)
    """
    Ajoute du texte sur une image existante et sauvegarde l'image modifiée.

    Args:
        image_path (str): Le chemin de l'image source à modifier.
        texte (str): Le texte à ajouter sur l'image.
        position (tuple): Position (x, y) où le texte sera ajouté sur l'image.
        output_path (str): Le chemin pour sauvegarder l'image modifiée.
        couleur (tuple, optional): La couleur du texte en format RGB. Par défaut noir (0, 0, 0).
        taille_police (int, optional): La taille de la police du texte. Par défaut 40.
        police (str, optional): Le chemin ou le nom du fichier de police TrueType (.ttf). Par défaut "arial.ttf".

    Returns:
        image

    Note:
        FileNotFoundError: Si le fichier d'image ou de police spécifié est introuvable.
        OSError: Si une erreur se produit lors de l'ouverture ou de la sauvegarde de l'image.
    """

    #Créer un objet de dessin pour manipuler l'image
    draw = ImageDraw.Draw(image)

    #Définir le texte à ajouter
    position = (100, 200)  #Position où le texte sera ajouté (x, y)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font = ImageFont.load_default()  #Utiliser une police par défaut si la police personnalisée n'est pas trouvée

    text_color = (255, 150, 255)
    draw.text(position, text, fill=text_color, font=font)
    return image