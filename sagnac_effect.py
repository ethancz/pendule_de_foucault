import numpy as np
import matplotlib.pyplot as plt

c = 299792458  # vitesse de la lumière en m/s
Omega_Terre = 2 * np.pi / 86164  # vitesse angulaire de la Terre en rad/s
print("Nous allons étudier le déphasage de Sagnac par rapport à un disque tournant")
R = float(input("\n\n  Veuillez donner la valeur (en mètre) du rayon du disque :"))
S = np.pi * (R ** 2)


def disque_relativite_restreinte(w):  # le paramètre est la vitesse angulaire du disque
    # delta représente le décalage temporel de 2 horloges synchronisées l'une se déplaçant \n
    # dans le sens de rotation du disque tournant et l'autre. Elles se déplacent le long de la circonférence du disque
    delta = (4 * np.pi * (R ** 2) * w) / (c ** 2 * np.sqrt(1 - (R ** 2 * w ** 2 / c ** 2)))
    return delta


i =np.arange(0, 20, 1)  #valeur de la vitesse angulaire, axe des abscisses
graph=disque_relativite_restreinte(i)   #valeur de delta en fonction des valeurs de i, la vitesse angulaire
point=disque_relativite_restreinte(Omega_Terre) #pour afficher le point d'abscisse Omega_Terre sur le graph
plt.xlabel('vitesse angulaire (en rad/s)')  #légende de l'axe des abscisses
plt.ylabel("décalage temporel de l'arrivé des horloges (en s)") #légende de l'axe des ordonnées
plt.legend() #légende du point
plt.title('Déphasage de Sagnac (en s) en fonction de la vitesse \nangulaire du disque tournant (en rad/s)', fontsize=13,pad=10)
plt.plot(Omega_Terre,point, marker="o", color="red", markersize=4, label="point ayant pour abscisse la \nvitesse de rotation de la Terre")
plt.plot(i,graph)
plt.show()

