# Créé par vstep, le 25/01/2019 en Python 3.4
#chargement des bibliothèques PIL et webbrowser
from PIL import Image
#chargement de l'image ( même dossier que le programme)
im = Image.open( 'velo.JPG' )
exif_data = im._getexif()
#on affiche les données exif
print(exif_data)

