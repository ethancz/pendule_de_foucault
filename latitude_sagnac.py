import numpy as np
import matplotlib.pyplot as plt

latitude = float(input("A quelle degré de latitude vous trouvez-vous (peu importe l'hémisphère)? : "))
teta = np.deg2rad(latitude)  # latitude en radian
R = 6378 * (10 ** 3)  # rayon de la terre en mètre
t = 86164  # temps en seconde que la terre met pour faire une rotation sur elle-même (23h56mn)
perimetre = 2 * np.pi * np.cos(teta) * R  # circonférence à la latitude donnée
perimetre = round(perimetre)
r_latitude = perimetre / (2 * np.pi)    # rayon à la latitude donné
r_latitude = round(r_latitude)
v = perimetre / t  # calcul de la vitesse à la latitude donnée en m/s
w=v/R     # w la vitesse angulaire à la latitude


print("\n\nle périmètre de cette latitude est de", perimetre / 1000, "km et votre vitesse à cette latitude est de", round(v), "m/s",
      "soit", round(v * 3.6), "km/h")
print("\n\nle rayon de cette latitude est de", r_latitude / 1000, "km")  # rayon à la latitude donnée en km
print("\n\nla vitesse angulaire est de w = ",w, "rad/s")

print("\n\nla valeur de la vitesse angulaire dépend donc de la latitude")







