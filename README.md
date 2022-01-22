# pendule_de_foucault
Science du numérique modélisation du pendule de foucault en python 

Pour le code _final_pendule.py_ j'utilise FFmpeg pour animer et enregistrer l'animation du pendule le site pour télécharger cette "extension" de python : https://www.gyan.dev/ffmpeg/builds/

Il faut ensuite décompresser l'archive et copier le chemin du dossier /bin contenant les fichiers .exe
Il faut mettre ce chemin dans vos varibale d'environnement, variable "path" .
Ensuite le programme devrait fonctionner

Ne pas oublier de changer la dernière ligne du code _final_pendule.py_ avec le chemin correspondant au dossier de votre projet.
L'animation enregistré s'ouvrira alors toute seule une fois que le fichier aura été créer
Cela peut prendre plusiseur dizaines de secondes selon la latitude (plus la période est grande plus le nombre de calcul sera grand)




Le fichier _latitude_sagnac.py_ permet de montrer que la vitesse angulaire d'un corps à la surface de la Terre est la même peu importe sa latitude, elle correspond à la vitesse angulaire de la Terre soit 2pi/86164 (exprimé en rad/s)

Finalement _sagnac_effect.py_ modélise sur un graph le décalage temporel de 2 horloges à la vitesse v0 se déplaçant le long d'un disque tourant à une vitesse angulaire w





