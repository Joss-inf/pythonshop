from PIL import Image
import logger
import os

import os
from PIL import Image

import os
from PIL import Image

def creer_gif(chemin_entrée, chemin_sortie, taille=(300, 300)):
    """
    Crée un GIF à partir des images d'un dossier, en redimensionnant les images à une taille commune.

    Args:
        chemin_entrée (str): Dossier contenant les images à inclure dans le GIF.
        chemin_sortie (str): Chemin du fichier GIF de sortie (doit inclure l'extension .gif).
        taille (tuple): Taille à laquelle toutes les images seront redimensionnées (largeur, hauteur). Par défaut (300, 300).
    
    Retour:
        None
    """
    # Vérifier si le dossier de sortie existe, sinon le créer
    output_dir = os.path.dirname(chemin_sortie)
    if not os.path.exists(output_dir) and output_dir:
        os.makedirs(output_dir)

    # Liste des images valides à inclure dans le GIF
    images = []
    #////////////commencement des verifs  du format d'image//////////////////////
    try:
        for filename in os.listdir(chemin_entrée):  # Parcours des fichiers dans le dossier source
            if filename.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")):  # Filtrer les images
                img_path = os.path.join(chemin_entrée, filename)  # Obtenir le chemin complet de l'image
                images.append(img_path)
        
        if not images:
            print("Erreur : Aucun fichier image valide trouvé dans le dossier.")
            return

    except FileNotFoundError:
        print(f"Erreur : Le dossier {chemin_entrée} n'a pas été trouvé.")
        return
    except PermissionError:
        print(f"Erreur : Impossible d'accéder à {chemin_entrée}. Vérifiez les permissions.")
        return
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return

    #////////////verification terminé du format d'image//////////////////////

    try:
        # Charger et redimensionner les images pour créer le GIF
        frames = []
        for image_path in images:
            img = Image.open(image_path)
            img = img.resize(taille)  # Redimensionner l'image à la taille spécifiée
            frames.append(img)

        # Vérifier que chemin_sortie contient un nom de fichier avec l'extension .gif
        if not chemin_sortie.lower().endswith('.gif'):
            print("Erreur : Le chemin de sortie doit avoir l'extension .gif.")
            return

        # Sauvegarder le GIF
        frames[0].save(
            chemin_sortie,
            save_all=True,
            append_images=frames[1:],
            duration=250,  # Durée en millisecondes pour chaque image dans le GIF
            loop=0
        )
        logger.log(f"GIF créé et sauvegardé sous : {chemin_sortie}")

    except FileNotFoundError:
        print(f"Erreur : Impossible de trouver les images dans {chemin_entrée}.")
    except PermissionError:
        print(f"Erreur : Impossible d'accéder à {chemin_sortie}. Vérifiez les permissions.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la création du GIF : {e}")



