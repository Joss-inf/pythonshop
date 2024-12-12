import os  # Pour la gestion des fichiers et dossiers
import sys  # Pour lire les arguments passés en ligne de commande
import grayFilter as gf  # Module custom pour appliquer un filtre gris
import rotateFilter as rf  # Module custom pour appliquer une rotation
import dilateEffect as de #Module custom pour appliquer un filtre de dilatation
import aquarelle as aqua #Module custom pour appliquer un filtre aquarelle
import bluring as b #Module custom pour appliquer un
import texteFilter as txt #Module custom pour ajouter du texte
import resizedimg as r #Module custom pour redimensionner
import GIF #Module custom pour crée des gifs
import logger as l  # Module custom pour enregistrer les logs
from PIL import Image # PIL pour le traitement des images

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
                          -aquarelle    : applique un filtre aquarelle sur l'image
    --gif pour générer des gifs , --i dossier d'entrée/ , --o dossier de sortie/ avec le nom du gif

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

        elif filter_action.startswith("text:"):
            # Applique du text si le filtre commence par "text:"
            try:
                text = str(filter_action.split(":")[1])  # Extraction du text
                image = txt.textFilter(image, text)  # Application du text
                l.log(f"text filter applied to {image} with text :{text}")
            except ValueError:
                # Gestion d'erreur si le text n'est pas un entier valide
                print(f"Erreur : text invalide pour le filtre '{filter_action}'.")

        elif filter_action == "blur":
            # Applique un filtre de flou
            image = b.bluring(image)

        elif filter_action.startswith("dilate:"):
            # Applique un effet de dilatation si le filtre commence par "dilate:"
            try:
                k = int(filter_action.split(":")[1])  # Extraction de la taille k
                image = de.apply_dilate_effect(image,k) # application de la dilatation
            except ValueError:
                # Gestion d'erreur si le text n'est pas un entier valide
                print(f"Erreur : k invalide pour le filtre '{filter_action}'.")
        elif filter_action == "aquarelle":
            image = aqua.apply_watercolor_and_oil_effect(image)
            l.log(f"aqua filter applied to {image}")
        elif filter_action.startswith("scale:"):
            # Applique un effet de dilatation si le filtre commence par "dilate:"
            try:
                k = float(filter_action.split(":")[1])  # Extraction de la mise à l'échelle
                image = r.resizedImg(image,k)
            except ValueError:
                # Gestion d'erreur si le text n'est pas un entier valide
                print(f"Erreur : scale invalide pour le filtre '{filter_action}'.")
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
                base_name, ext = os.path.splitext(filename)  # Sépare le nom de base et l'extension
                #on renomme l'image en ajourant le mot "modified"
                new_name = f"{base_name}_modified{ext}"

                output_path = os.path.join(output_dir, new_name)  # Chemin complet de sortie
                modified_image.save(output_path)  # Sauvegarde l'image modifiée
            except Exception as e:
                # Gestion des exceptions pendant le traitement de l'image
                print(f"Erreur lors du traitement de l'image {filename} : {e}")

def read_config_file(config_file):
    """
    Lit les paramètres d'un fichier de configuration.

    Parameters:
    - config_file (str): Chemin vers le fichier de configuration.
    Exemple de fichier de configuration (--config) :
     filters=gray&blur
     input=input/
     output=output/

    Returns:
    - Un dictionnaire contenant les paramètres (filters, input, output).
    """
    # Initialisation d'un dictionnaire `config` avec des clés par défaut et des valeurs vides.
    config = {"filters": "", "input": "", "output": ""}
    try:
        # Tentative d'ouverture du fichier spécifié par `config_file` en mode lecture.
        with open(config_file, "r") as file:
            # Parcours de chaque ligne du fichier.
            for line in file:
                # Séparation de la ligne en deux parties : clé et valeur, en supposant qu'elles sont séparées par un "=".
                key, value = line.strip().split("=")
                # Suppression des espaces inutiles et ajout de la paire clé-valeur dans le dictionnaire `config`.
                config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {config_file} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier {config_file} : {e}")
    return config

def main()->None:
    """
    Point d'entrée principal pour la CLI.
    Lit les arguments de la ligne de commande et exécute les actions appropriées.
    """
    if len(sys.argv) <= 2 or  str(sys.argv[1]) != "image-filter":
        print("wrong command, refer to ->image-filter --help<-")
        return
    a2 = str(sys.argv[2])  # Premier argument de la ligne de commande
    if  len(sys.argv) == 8 and a2 == "--filters"  and sys.argv[4] == "--i" and sys.argv[6] == "--o":
        # Cas où les arguments sont correctement structurés
        filters = sys.argv[3]  # Récupère les filtres
        infold = sys.argv[5]  # Dossier source
        outfold = sys.argv[7]  # Dossier destination
        process_images(infold, outfold, filters)  # Applique le traitement
        return
    elif len(sys.argv) == 7 and a2 == "--gif" and sys.argv[3] == "--i" and sys.argv[5] == "--o":
        infold = sys.argv[4]
        outfold = sys.argv[6]
        GIF.creer_gif(infold, outfold)
    elif a2 == "--help":
        # Cas où l'utilisateur demande l'aide
        help()
        return

    elif a2 == "--config":
        if len(sys.argv) < 4:
            print("Erreur : Aucun fichier de configuration spécifié.")
            return
        config_file = sys.argv[3]
        config = read_config_file(config_file)
        if not all(config.values()):
            print("Erreur : Le fichier de configuration est incomplet.")
            return
        process_images(config["input"], config["output"], config["filters"])
    else:
        print("Commande invalide. Utilisez '--help' pour plus d'informations.")


if __name__ == "__main__":
    main()  # Lance le programme
