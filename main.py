import os  # Pour la gestion des fichiers et dossiers
import sys  # Pour lire les arguments passés en ligne de commande
import grayFilter as gf  # Module custom pour appliquer un filtre gris
import rotateFilter as rf  # Module custom pour appliquer une rotation
import logger as l  # Module custom pour enregistrer les logs
from PIL import Image, ImageFilter  # PIL pour le traitement des images

def help():
    return print(
    """
    Options:
    --filters "FILTERS"   Applique une chaîne de filtres séparés par '&'.
                        Filtres disponibles :
                          - gray         : Convertit l'image en niveaux de gris.
                          - rotate:DEGRE : Tourne l'image de l'angle spécifié (en degrés).
                          - blur         : Applique un flou sur l'image.
                          - text:TXT     : Ajoute le texte TXT sur l'image.
                          - dilate:N     : Applique un effet de dilatation avec une taille N.
                          - scale:N      : Redimensionne l'image avec un facteur de N.

  --i INPUT/            Spécifie le dossier source contenant les images à traiter.
                        Exemple : --i input/

  --o OUTPUT/           Spécifie le dossier où sauvegarder les images modifiées.
                        Exemple : --o output/

  --config CONFIG_FILE  Spécifie un fichier de configuration contenant les paramètres 
                        des filtres et des dossiers. Le fichier doit être au format texte, 
                        avec une ligne par option (exemple ci-dessous).

  --help                Affiche cette aide.

Exemple d'utilisation :
  image-filter --filters "gray&rotate:55" --i input/ --o output/

Exemple de fichier de configuration (--config) :
  filters=gray&blur
  input=input/
  output=output/
""")


def apply_filters(image, filters):
    """
    Applique les filtres spécifiés à une image.

    Parameters:
    - image: L'objet PIL.Image.
    - filters (str): Liste de filtres séparés par "&" (ex: "gray&rotate:45").

    Returns:
    - Image modifiée.
    """
    for filter_action in filters.split("&"):  # Séparer les filtres par "&"
        if filter_action == "gray":
            # Applique un filtre gris à l'image
            image = gf.gray_filter(image)
            l.log(f"gray filter applied to {image}")

        elif filter_action.startswith("rotate:"):
            # Applique une rotation si le filtre commence par "rotate:"
            try:
                dgr = int(filter_action.split(":")[1])  # Extraction de l'angle
                image = rf.rotateImg(image, dgr)  # Application de la rotation
                l.log(f"rotary filter applied to {image} at {dgr} dgr")
            except ValueError:
                # Gestion d'erreur si l'angle n'est pas un entier valide
                print(f"Erreur : Angle invalide pour le filtre '{filter_action}'.")

        elif filter_action == "blur":
            # Applique un flou à l'image
            image = image.filter(ImageFilter.BLUR)

        elif filter_action == "sharpen":
            # Applique un filtre de netteté
            image = image.filter(ImageFilter.SHARPEN)

        elif filter_action == "dilate":
            # Applique un effet de dilatation
            image = image.filter(ImageFilter.MaxFilter(size=3))

        else:
            # Message d'erreur si un filtre est inconnu
            print(f"Filtre inconnu : {filter_action}")

    return image  # Retourne l'image modifiée

def process_images(input_dir, output_dir, filters):
    """
    Applique les filtres aux images d'un dossier source et les sauvegarde dans un dossier destination.

    Parameters:
    - input_dir (str): Dossier source.
    - output_dir (str): Dossier destination.
    - filters (str): Liste de filtres à appliquer.
    """
    if not os.path.exists(output_dir):  # Vérifie si le dossier destination existe
        os.makedirs(output_dir)  # Crée le dossier si nécessaire

    for filename in os.listdir(input_dir):  # Parcours de tous les fichiers dans le dossier source
        if filename.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")):
            # Filtrage pour ne traiter que les fichiers image
            try:
                img_path = os.path.join(input_dir, filename)  # Chemin complet de l'image
                image = Image.open(img_path)  # Charge l'image

                modified_image = apply_filters(image, filters)  # Applique les filtres

                output_path = os.path.join(output_dir, filename)  # Chemin complet de sortie
                modified_image.save(output_path)  # Sauvegarde l'image modifiée
                print(f"Image sauvegardée : {output_path}")
            except Exception as e:
                # Gestion des exceptions pendant le traitement de l'image
                print(f"Erreur lors du traitement de l'image {filename} : {e}")

def main()->None:
    """
    Point d'entrée principal pour la CLI.
    Lit les arguments de la ligne de commande et exécute les actions appropriées.
    """
    if sys.argv[1] != "image-filter":
        print("wrong command, refer to ->image-filter --help<-")
        return
    a2 = sys.argv[2]  # Premier argument de la ligne de commande
    if a2 == "--filters" and sys.argv[4] == "--i" and sys.argv[6] == "--o":
        # Cas où les arguments sont correctement structurés
        filters = sys.argv[3]  # Récupère les filtres
        infold = sys.argv[5]  # Dossier source
        outfold = sys.argv[7]  # Dossier destination
        process_images(infold, outfold, filters)  # Applique le traitement
        return

    elif a2 == "--help":
        # Cas où l'utilisateur demande l'aide
        help()
        return

    elif a2 == "--config":
        # Cas où l'utilisateur passe une configuration
        text_config = sys.argv[2]  # Lecture d'un fichier de config (non implémenté ici)
        print(f"Configuration chargée : {text_config}")
        return
    print("wrong command, refer to ->image-filter --help<-")
if __name__ == "__main__":
    main()  # Lance le programme
