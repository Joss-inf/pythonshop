from PIL import Image, ImageFilter
#import logger

def apply_dilate_effect(input_path: str, output_path: str = None, k_size: int = 3):
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
        # Charger l'image
        img = Image.open(input_path)
        
        # Convertir en niveaux de gris (optionnel)
        img = img.convert("L")
        
        # Appliquer l'effet de dilatation
        dilated_img = img.filter(ImageFilter.MaxFilter(size=k_size))
        
        # Afficher le résultat
        dilated_img.show()

        # Sauvegarder l'image si un chemin est spécifié
        if output_path:
            dilated_img.save(output_path)
            print(f"Image sauvegardée à : {output_path}")
        
        return dilated_img
    #logger.log(f"le filtre de dilatation à été appliqué a l'image")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_path} n'a pas été trouvé.")
    except PermissionError:
        print(f"Erreur : Impossible d'accéder à {input_path}. Vérifiez les permissions.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

