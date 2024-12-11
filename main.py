import os,sys
import grayFilter as gf
import rotateFilter as rf
from PIL import Image, ImageFilter

def apply_filters(image, filters):
    """
    Applique les filtres spécifiés à une image.

    Parameters:
    - image: L'objet PIL.Image.
    - filters (str): Liste de filtres séparés par "&" (ex: "gray&rotate:45").

    Returns:
    - Image modifiée.
    """
    for filter_action in filters.split("&"):
        if filter_action == "gray":
            image = gf.gray_filter(image)
        elif filter_action.startswith("rotate:"):
            try:
                image = rf.rotateImg(image,int(filter_action.split(":")[1]))
            except ValueError:
                print(f"Erreur : Angle invalide pour le filtre '{filter_action}'.")
        elif filter_action == "blur":
            image = image.filter(ImageFilter.BLUR)
        elif filter_action == "sharpen":
            image = image.filter(ImageFilter.SHARPEN)
        elif filter_action == "dilate":
            image = image.filter(ImageFilter.MaxFilter(size=3))
        else:
            print(f"Filtre inconnu : {filter_action}")
    return image

def process_images(input_dir, output_dir, filters):
    """
    Applique les filtres aux images d'un dossier source et les sauvegarde dans un dossier destination.

    Parameters:
    - input_dir (str): Dossier source.
    - output_dir (str): Dossier destination.
    - filters (str): Liste de filtres à appliquer.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(("png", "jpg", "jpeg", "bmp", "gif")):
            try:
                # Charger l'image
                img_path = os.path.join(input_dir, filename)
                image = Image.open(img_path)

                # Appliquer les filtres
                modified_image = apply_filters(image, filters)

                # Sauvegarder l'image modifiée
                output_path = os.path.join(output_dir, filename)
                modified_image.save(output_path)
                print(f"Image sauvegardée : {output_path}")
            except Exception as e:
                print(f"Erreur lors du traitement de l'image {filename} : {e}")

def main():
    a1=sys.argv[1]
    if a1 == "--filters" and sys.argv[3] == "--i" and sys.argv[5] == "--o":
        print("bamboulax")
        filters = sys.argv[2]
        infold = sys.argv[4]
        outfold = sys.argv[6]
        process_images(infold,outfold,filters)
        return
    elif a1 == "--help":
        help()
        return
    elif a1 == "--config":
        text_config = sys.argv[2]

if __name__ == "__main__":
    main()
