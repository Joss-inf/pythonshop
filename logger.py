import datetime

def log(m:str = ""):
    try:
        with open('image.log','a') as f:
            f.write(m+" "+str(datetime.datetime.now()).split('.')[0] + "\n")
    except FileNotFoundError:
        print("Erreur : Le fichier 'movie.log' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
