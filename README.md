# PythonShop - Une Alternative de Photoshop en Ligne de Commande

Bienvenue dans **PythonShop**, une application simple et puissante pour traiter vos images directement depuis la ligne de commande. PythonShop vous permet d'appliquer des filtres variés à vos images, de les redimensionner, d'ajouter du texte, de créer des GIFs, et bien plus encore. Idéal pour les développeurs et amateurs souhaitant une alternative rapide et personnalisable à Photoshop.

---

## Présentation

Avec notre éditeur de photos, vous pouvez :
- Ajouter des filtres tels que :
  - **Flou**
  - **Monochrome**
  - **Aquarelle**
  - **Dilatation**
  - **Noir et Blanc**
- Faire pivoter l'image sélectionnée.
- Découper ou redimensionner vos images.
- Écrire sur l'image.

Après chaque modification, l'image mise à jour sera automatiquement sauvegardée sur votre appareil.

---

## Fonctionnalités principales

### Filtres disponibles
- **Flou** : Adoucissez les contours pour un effet artistique ou professionnel.
- **Monochrome** : Transformez vos images en noir et blanc intemporels.
- **Aquarelle** : Donnez à vos photos une touche de peinture artistique.
- **Noir et Blanc** : Convertit l'image en niveaux de gris.

### Manipulation d'images
- **Rotation** : Faites pivoter vos images dans n'importe quelle direction.
- **Découpe et redimensionnement** : Ajustez la taille et le cadrage de vos photos à vos besoins.

---

## Tutoriel d'Installation

### Prérequis

- **Python 3.10 ou version supérieure**
- Une connexion Internet pour installer les dépendances

### Installation des Librairies

Pour exécuter PythonShop, vous devez installer quelques librairies Python nécessaires. Exécutez la commande suivante dans votre terminal apres avoir telechargé pythonshop:

```bash
pip install .requirement
```
ou
```bash
pip install pillow
```


**Modules personnalisés requis :** Assurez-vous que les fichiers suivants se trouvent dans le même répertoire que le script principal :

- `grayFilter.py`
- `rotateFilter.py`
- `dilateEffect.py`
- `aquarelle.py`
- `bluring.py`
- `texteFilter.py`
- `resizedimg.py`
- `GIF.py`
- `logger.py`

### Cloner le Dépôt Git

Pour récupérer le code source, utilisez la commande suivante :

```bash
git clone git@github.com:Joss-inf/pythonshop.git
```

---

## Tutoriel d'Utilisation

### Lancer PythonShop

La commande principale pour lancer PythonShop est :

```bash
python pythonshop.py image-filter [OPTIONS]
```

### Options Disponibles

1. **Filtres** :

   ```bash
   --filters "gray&rotate:45&blur"
   ```

   - **gray** : Convertit l'image en niveaux de gris
   - **rotate*:DEGRE : Fait pivoter l'image d'un certain angle (en degrés)
   - **blur** : Applique un effet de flou
   - **text**:TXT : Ajoute du texte sur l'image
   - **dilate**:N\ : Applique un effet de dilatation avec une taille N
   - **scale**:N : Redimensionne l'image par un facteur N
   - **aquarelle** : Applique un effet aquarelle

2. **Génération de GIFs** :

   ```bash
   --gif --i chemin_dossier_images --o chemin_fichier_sortie
   ```

   Combine plusieurs images dans un dossier pour créer un GIF.

3. **Utilisation d'un Fichier de Configuration** :

   ```bash
   --config chemin_du_fichier_config
   ```

   Exemple de fichier de configuration :

   ```
   filters=gray&blur
   input=input_folder/
   output=output_folder/
   ```

4. **Afficher l'Aide** :

   ```bash
   --help
   ```

### Exemple d'Utilisation

1. Convertir une image en niveaux de gris et la faire pivoter de 90 degrés :
   ```bash
   python pythonshop.py image-filter --filters "gray&rotate:90" --i input/ --o output/
   ```
2. Créer un GIF à partir d'un dossier :
   ```bash
   python pythonshop.py image-filter --gif --i images/ --o animation.gif
   ```

---

## Documentation des Fonctions

### `apply_filters(image, filters)`

Applique une série de filtres à une image donnée.

- **Paramètres :**
  - `image` : Objet PIL.Image à traiter
  - `filters` : Chaîne de filtres séparés par `&`
- **Retour :** Image modifiée

### `process_images(input_dir, output_dir, filters)`

Applique les filtres à toutes les images d'un dossier source et les sauvegarde dans un dossier de destination.

- **Paramètres :**
  - `input_dir` : Chemin du dossier contenant les images d'origine
  - `output_dir` : Chemin du dossier de sortie
  - `filters` : Liste des filtres à appliquer

### `read_config_file(config_file)`

Lit les paramètres d'un fichier de configuration spécifié.

- **Paramètres :**
  - `config_file` : Chemin vers le fichier de configuration
- **Retour :** Dictionnaire contenant les paramètres `filters`, `input`, et `output`

---

## Remerciements

Merci d'avoir choisi PythonShop. Nous espérons que vous apprécierez l'expérience et les fonctionnalités offertes !

---

## Auteurs

- Josselin
- Adam
- Antoine
- Mathis

N'hésitez pas à proposer des idées ou à contribuer au projet !