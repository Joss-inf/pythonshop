from PIL import Image, ImageDraw, ImageFont

# Charger votre image existante
image_path = "entrée/KAARIS OR NOIR.jpg"  # Remplacez par le chemin de votre image
image = Image.open(image_path)

# Créer un objet de dessin pour manipuler l'image
draw = ImageDraw.Draw(image)

# Définir le texte à ajouter
text = "UwU"
position = (100, 200)  # Position où le texte sera ajouté (x, y)

# Charger une police
try:
    font = ImageFont.truetype("arial.ttf", 40)  # Spécifiez le fichier de police .ttf
except IOError:
    font = ImageFont.load_default()  # Utiliser une police par défaut si la police personnalisée n'est pas trouvée

# Ajouter le texte sur l'image
text_color = (255, 150, 255)  # Couleur du texte en RGB (ici rouge)
draw.text(position, text, fill=text_color, font=font)

# Sauvegarder ou afficher l'image modifiée
image.show()  # Affiche l'image dans une visionneuse
image.save("KAKAKAKAKAKAKRIS.jpg")  # Sauvegarde l'image modifiée