
from PIL import Image, ImageFilter, ImageEnhance
#import logger

def apply_watercolor_and_oil_effect(img):
    """
    Applique un effet aquarelle et un effet huilé à une image, puis la sauvegarde sous un nouveau nom.

    :param input_file: Chemin du fichier d'entrée (image source).
    :param output_file: Chemin du fichier de sortie (image avec effets).
    """
    try:
        # Ouvrir l'image

        # Étape 1 : Appliquer un flou pour lisser les couleurs
        img_blurred = img.filter(ImageFilter.GaussianBlur(radius=2))

        # Étape 2 : Renforcer les bords sur l'image floutée pour simuler des traits artistiques
        img_edges = img_blurred.filter(ImageFilter.EDGE_ENHANCE_MORE)

        # Étape 3 : Combiner le flou et les bords pour un effet pictural
        img_combined = Image.blend(img_blurred, img_edges, alpha=0)

        # Étape 4 : Améliorer les couleurs pour les rendre plus vibrantes
        enhancer = ImageEnhance.Color(img_combined)
        img_vibrant = enhancer.enhance(1.5)

        # Étape 5 : Ajouter un effet huilé (filtre ModeFilter)
        img_oil = img_vibrant.filter(ImageFilter.ModeFilter(size=18))
        return img_oil
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

