import math
from math import *
import numpy as np

Omega = (2 * pi) / 86164  # vitesse de rotation de la terre en rad/s
teta = float(input("A quelle latitude voulez vous observez le pendule de Foucault ? :"))
radian = math.radians(teta)  # conversion de la latitude de degré en radian
while (radian > 2 * pi):  # modulo 2pi
    radian -= 2 * pi
while (radian < 0):
    radian += 2 * pi

def calculPeriode():
    periode = (2*pi)/(Omega*sin(radian))
    periode_h = periode/float(3600)         #conversion de la période en secondes en heures décimales
    periode_h=round(periode_h,3)
    h,m=str(periode_h).split(".")           #on divise les heures pour récupérer séparément la partie entière (les heures) et la parties décimale (mintures seconde)
    h =int(h); m = int(m)                   #conversion de str vers int pour manipuler les nombres
    heure = h
    m = (m/1000)*60                         #conversion de la partie décimale en minutes décimales
    m,s=str(m).split(".")                   #conversion des minutes décimales en minutes et secondes
    m=int(m);s=int(s)
    minutes = m
    secondes = (s/1000)*60                  #conversion en secondes décimales
    print('la période du pendule de foucault à cette latitude est ', heure, 'h', minutes, 'minutes', round(secondes), 's')
    return (periode, heure, minutes, secondes)

calculPeriode()

