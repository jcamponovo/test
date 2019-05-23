# Créé par vstep, le 25/01/2019 en Python 3.4
#chargement des bibliothèques PIL et webbrowser
from PIL import Image
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
# le 1er tuple ( degré, 1) le second ( minute,1) le 3ème ( seconde,100)
# on divise le 1er par le second et on transforme en degré

# affichage des coordonnées au format décimal
lat_deg=test[2][0][0]/test[2][0][1]
lat_min=test[2][1][0]/test[2][1][1]/60
lat_sec=test[2][2][0]/test[2][2][1]/3600
lat=lat_deg+lat_min+lat_sec
print("la latitude est: ")
print(lat)
# idem
lon_deg=test[4][0][0]/test[4][0][1]
lon_min=test[4][1][0]/test[4][1][1]/60
lon_sec=test[4][2][0]/test[4][2][1]/3600
lon=lon_deg+lon_min+lon_sec
print("la longitude est: ")
print(lon)


