from PIL import Image

def BL_Filter(file:str):

    try:
        # Ouvrir l'image
        img = Image.open(file)

        # Convertir l'image en niveaux de gris
        img = img.convert("L")  # L pour converion en Luminance (noir et blanc)

        # sauvegarder l'image
        folder:str = "sortie"
        img.save(folder+'/BL_'+file)

    #gestion d'erreur
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

BL_Filter("profil-img.png")
