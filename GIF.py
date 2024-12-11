from PIL import Image

def creer_gif(images, chemin_sortie, duree):
    """
    Crée un GIF à partir d'une liste d'images.
    
    Args:
        images (list): Liste des chemins des images.
        chemin_sortie (str): Chemin de sortie du GIF.
        duree (int): Durée de chaque image en millisecondes.
    """
    # Charger toutes les images
    frames = [Image.open(image) for image in images]

    # Sauvegarder les images sous forme de GIF
    frames[0].save(
        chemin_sortie,
        save_all=True,
        append_images=frames[1:],
        duration=duree,
        loop=0
    )
    print(f"GIF créé et sauvegardé sous : {chemin_sortie}")

if __name__ == "__main__":
    images = ["KAARIS OR NOIR.jpg", "BBB.jpg", "NINHO.jpg"] 
    
    chemin_sortie = "KAARIS.gif"
    
    duree = 500  # 500 ms = 0,5 seconde par image
    
    creer_gif(images, chemin_sortie, duree)
