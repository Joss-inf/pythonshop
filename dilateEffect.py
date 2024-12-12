from PIL import Image, ImageFilter
import logger

def apply_dilate_effect(img, k_size: int = 3):
    """
    Applique un effet de dilatation à une image et gère les erreurs.

    Parameters:
    - input_path (str): Chemin de l'image source.
    - output_path (str): Chemin pour sauvegarder l'image dilatée (optionnel).
    - k_size (int): Taille du noyau pour la dilatation (par défaut : 3x3).

    Returns:
    - Image avec l'effet de dilatation appliqué.
    """
    try:

        # Convertir en niveaux de gris (optionnel)

        # Appliquer l'effet de dilatation
        dilated_img = img.filter(ImageFilter.MaxFilter(size=k_size))

        logger.log(f"le filtre de dilatation à été appliqué a l'image: {dilated_img}")
        return dilated_img

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

