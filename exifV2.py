# Créé par vstep, le 25/01/2019 en Python 3.4
#chargement des bibliothèques PIL et webbrowser
from PIL import Image
import webbrowser
#chargement de l'image ( même dossier que le programme)
im = Image.open( 'velo.JPG' )
# chargement des données exif, c'est un dictionnaire les données gps sont à la clé 34853
# repéré à l'aide de l'explorateur de variable de l'ide python
exif_data = im._getexif()
#chargement des données de la clé 34853
# on crée un dictionnaire pour contenir les données GPS
test={}
test=exif_data[34853]
# eplorer la variable test pour savoir comment elle est structurée
# ce dico contient des listes
# la latitude est à la clé 2 qui est une liste de tuples
# le 1er tuple ( degré, 1) le second ( minute,1) le 3ème ( seconde,4096)
# on divise le 1er par le second et on transforme en degré
print(test)


