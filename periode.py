from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

z0 = 1      #position initiale du pendule en mètre à t=0
Omega = ((2 * np.pi) / 86164)  # vitesse de rotation de la Terre (qui sera ensuite multipliée par 200 pour rendre l'animation plus visible et compréhensible)
l = 67      #longueur de la corde du pendule en mètre
g = 9.81    #intensité du champ de pesanteur à la surface de la Terre (en m.s^-2)
latitude = float(input("A quelle latitude voulez vous observez le pendule de Foucault ? :"))
teta = np.deg2rad(latitude)  # conversion de la latitude de degré en radian
while (teta > 2 * np.pi):  # modulo 2pi
    teta -= 2 * pi
while (teta < 0):
    teta += 2 * pi

w = np.sqrt(g / l)
w0 = np.sqrt(np.square(w) + np.square(Omega) * np.square(np.sin(teta)))
t = np.arange(0, 215, 1)


def calculPeriode():
    periode = (2 * pi) / (Omega * sin(teta))
    periode_h = periode / float(3600)  # conversion de la période en secondes en heures décimales
    periode_h = round(periode_h, 3)
    h, m = str(periode_h).split(".")  # on divise les heures pour récupérer séparément la partie entière (les heures) et la partie décimale (minutes et secondes)
    h = int(h)
    m = int(m)  # conversion de str vers int pour manipuler les nombres
    heure = h
    m = (m / 1000) * 60  # conversion de la partie décimale en minutes décimales
    m=round(m,2)
    m, s = str(m).split(".") # conversion des minutes décimales en minutes et secondes
    m = int(m)
    s = int(s)
    minutes = m
    secondes = (s / 100) * 60  # conversion en secondes décimales
    print(secondes)
    secondes = round(secondes,1)
    print('la période du pendule de foucault à cette latitude est ', heure, 'h', minutes, 'minutes et', round(secondes),'secondes soit', round(periode), 'secondes')
    return (periode, heure, minutes, secondes,Omega)

def graph_pendule():

    Omega_accelere = Omega * 200

    # fonction
    e = (-1) * 1j * Omega_accelere * np.sin(teta) * t
    e = np.exp(e)
    a = (np.cos(w0 * t) + ((1j * Omega_accelere * np.sin(teta) * np.sin(w0 * t)) / w0))
    z = z0 * e * a

    X = z.real  # partie réelle de z
    Y = z.imag  # partie imaginaire de z

    X=X.tolist()
    Y=Y.tolist()


    # limite des axes
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # affichage de la courbe
    plt.plot(X,Y,'green')
    plt.grid()
    plt.show()

    # z0*np.cos(w0*t)
    # (z0*Omega*np.sin(teta)*np.sin(w0*t))/w0
    # 210*(2*np.pi)/86164
    return X,Y

calculPeriode()
graph_pendule()
