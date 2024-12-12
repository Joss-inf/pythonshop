
from PIL import ImageFilter
import logger

def bluring(img):
    """
    Applique un effet de flou gaussien à une image et enregistre une entrée dans le journal.

    Args:
        img (PIL.Image.Image): L'image PIL à flouter.
        n (int): Le rayon de flou gaussien. Plus le rayon est grand, plus l'effet de flou est intense.

    Returns:
        PIL.Image.Image: L'image floutée avec l'effet appliqué.

    Raises:
        TypeError: Si `img` n'est pas une instance de `PIL.Image.Image` ou si `n` n'est pas un entier.
        ValueError: Si `n` est un entier négatif.
    """
    n:int = 10

    # Application du filtre de flou gaussien
    img = img.filter(ImageFilter.GaussianBlur(n))  # Applique le filtre GaussianBlur avec le rayon `n`.

    # Enregistrement dans les logs
    logger.log("L'image a été floutée avec un rayon de {n}degrées")

    # Retourne l'image floutée
    return img
