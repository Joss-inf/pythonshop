from PIL import Image
import logger
def creer_gif(images, chemin_sortie, duree):
    """
    Crée un GIF à partir d'une liste d'images.
    
    Args:
        images (list): Liste des chemins des images.
        chemin_sortie (str): Chemin de sortie du GIF.
        duree (int): Durée de chaque image en millisecondes.
    
    Return:
        les images transformées en GIF.
    """
    try:
        #charge l'image
        frames = [Image.open(image) for image in images]

        frames[0].save(
            chemin_sortie,
            save_all=True,
            append_images=frames[1:],
            duration=duree,
            loop=0
        )
        print(f"GIF créé et sauvegardé sous : {chemin_sortie}")
        logger.log(f"le GIF a été généré avec succès")

        if __name__ == "__main__":
            images = ["KAARIS OR NOIR.jpg", "BBB.jpg", "NINHO.jpg"] 
            
            chemin_sortie = "KAARIS.gif"
            
            duree = 250  #en ms
            
            creer_gif(images, chemin_sortie, duree)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {images} n'a pas été trouvé.")
    except PermissionError:
        print(f"Erreur : Impossible d'accéder à {chemin_sortie}. Vérifiez les permissions.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


