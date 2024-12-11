import datetime

def log(m:str = "")->None:
    try:
        with open('image.log','a') as f:
            f.write(m+" "+str(datetime.datetime.now()).split('.')[0] + "\n")
    except FileNotFoundError:
        print("Erreur : Le fichier 'movie.log' n'existe pas.")
    except IOError as e:
        print(f"Erreur lors de l'ouverture ou de la sauvegarde du fichier : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
