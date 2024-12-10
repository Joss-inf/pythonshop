from PIL import Image


def rotateImg(dgr:int) ->None:

    if dgr <0 or dgr >360:
        print("error wrong degrees")
        return

    try:
        file = 'profil-img.png'
        folder = 'sortie/'
        img = Image.open(file)
        rotated_image = img.rotate(dgr)
        rotated_image.save(folder+f'rotate_{dgr}dgr_'+file)

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
