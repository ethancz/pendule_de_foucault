from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
from os import startfile

z0 = 1  # position initiale du pendule en mètre à t=0
Omega = ((
                 2 * np.pi) / 86164)  # vitesse de rotation de la Terre (qui sera ensuite multipliée par 200 pour rendre l'animation plus visible et compréhensible)
l = 67  # longueur de la corde du pendule en mètre
g = 9.81  # intensité du champ de pesanteur à la surface de la Terre (en m.s^-2)
latitude = float(input("A quelle latitude voulez vous observez le pendule de Foucault ? :"))
teta = np.deg2rad(latitude)  # conversion de la latitude de degré en radian

# while (teta > 2 * np.pi):  # modulo 2pi
#    teta -= 2 * pi
# while (teta < 0):
#   teta += 2 * pi
if teta == 0 and latitude == 0:  # pour éviter l'erreur de division par 0 on a ici une condition spéciale concernant le pendule à l'équateur qui tend vers l'infini
    teta = np.deg2rad(0.1)
    print("\n Le pendule est à l'équateur, sa période oscillation tend vers l'infini")

    plt.axhline(y=0)
    plt.title("Oscillation du pendule à l'équateur")
    plt.xlim(-1, 1)  # limite du graphique en x
    plt.ylim(-1, 1)  # limite du graphique en y

    plt.grid()
    plt.show()
    exit()

elif latitude == 90 or teta == np.pi / 2:
    print(
        "\n Le pendule est à un des pôles, sa période d'oscillation correspond à la période d'oscillation de la terre ")

hemisphere = str(input('Dans quel hémisphère se trouve votre position géographique? \n Nord(N) ou Sud(S) :'))
if hemisphere.lower() == "n":
    hemisphere = 1
elif hemisphere.lower() == "s":
    hemisphere = -1

w = np.sqrt(g / l)
w0 = np.sqrt(np.square(w) + np.square(Omega) * np.square(np.sin(teta)))

periode = (2 * pi) / (Omega * sin(teta))


def calculPeriode():
    periode_h = periode / float(3600)  # conversion de la période en secondes en heures décimales
    periode_h = round(periode_h, 3)
    h, m = str(periode_h).split(
        ".")  # on divise les heures pour récupérer séparément la partie entière (les heures) et la partie décimale (minutes et secondes)
    h = int(h)
    m = int(m)  # conversion de str vers int pour manipuler les nombres
    heure = h
    m = (m / 1000) * 60  # conversion de la partie décimale en minutes décimales
    m = round(m, 2)
    m, s = str(m).split(".")  # conversion des minutes décimales en minutes et secondes
    m = int(m)
    s = int(s)
    minutes = m
    secondes = (s / 100) * 60  # conversion en secondes décimales
    secondes = round(secondes, 1)
    print('la période du pendule de foucault à cette latitude est ', heure, 'h', minutes, 'minutes et', round(secondes),
          'secondes soit', round(periode), 'secondes')
    return heure, minutes, secondes, Omega, periode


periode_new = round(periode / 200)

t = np.arange(0, periode_new,
              1)  # temps entre 0 et la période divisé par 200 avec un pas de 1, cela correspond à t(0), t(1), t(2) jusqu'à t(période/200)


def graph_pendule():
    Omega_accelere = Omega * 200
    w0_ = w0
    z0_ = z0
    latitude_ = int(latitude)  # nouvelle variable pour afficher la latitude sur le titre du graph

    # fonction du pendule de foucault
    e = (-1) * 1j * Omega_accelere * np.sin(teta) * t
    e = np.exp(e)
    a = (np.cos(w0_ * t) + ((1j * Omega_accelere * np.sin(teta) * np.sin(w0_ * t)) / w0))
    z = z0 * e * a

    X = z.real  # partie réelle de z
    Y = hemisphere * z.imag  # partie imaginaire de z
    # la variable hémisphère sert à donner ou non l'opposé de la force de Coriolis selon si on se trouve sur l'hémisphère nord ou sud

    liste_X = []  # création d'une liste vide
    liste_Y = []  # création d'une liste vide

    # limite des axes
    plt.xlim(-1, 1)  # limite du graphique en x
    plt.ylim(-1, 1)  # limite du graphique en y

    # affichage de la courbe
    plt.plot(X, Y, 'blue')
    plt.grid()
    plt.title(f"Oscillation du pendule de Foucault à la latitude %d$°$" % latitude_)
    plt.show()

    # Définir le writer
    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Pendule de Foucault', artist='APP G9A',
                    comment='pendule de Foucault en python G9A')
    writer = FFMpegWriter(fps=5, metadata=metadata)  # on définit le nombre de calculs par secondes (frames)

    # Initialise l'animation
    fig = plt.figure()

    # on trace la courbe
    f=z0_
    g=0
    triangle, = plt.plot(f, g,'y<',markersize=10, label='Position de départ du pendule')
    angle_cercle = np.linspace(0, 2 * np.pi,
                               180)  # création d'un cercle de rayon z0 pour que les oscillations du pendule apparaissent dedans, " un peu comme au Panthéon, en 1851"
    rayon = z0_
    c = rayon * np.cos(angle_cercle)
    d = rayon * np.sin(angle_cercle)
    circle, = plt.plot(c, d, 'k')  # affichage du cercle
    courbe, = plt.plot(X, Y, 'b-', markersize=10, label= 'Tracés des oscillations du pendules')  # affichage des oscillations
    red_dot, = plt.plot(X, Y, 'ro', markersize=12, label= 'Boule du pendule')  # affichage du point qui modélise la boule du pendule
    plt.axis(
        "equal")  # pour que le graph soit proportionnel et pour ne pas afficher un cercle applati, égalise le pas de chaque axe
    plt.xlabel('X')  # on nomme les axes en fonction des affixes de z, ici X la partie réelle
    plt.ylabel('Y')  # on nomme les axes en fonction des affixes de z, ici Y la partie imaginaire
    plt.title(f"Oscillation du pendule de Foucault à la latitude %d$°$" % latitude_) #titre qui varie en fonction de la variable 'latitude' entrée par l'utilisateur
    
    #configuration de la légende
    leg_1=plt.legend(handles=[triangle], loc='upper right',fontsize=6)
    leg_2=plt.legend(handles=[red_dot], loc='upper left',fontsize=6)
    leg_3=plt.legend(handles=[courbe], loc='lower right',fontsize=6)
    fig.add_artist(leg_1)
    fig.add_artist(leg_2)
    fig.add_artist(leg_3)



    # configuration de l'enregistrement de l'animation
    with writer.saving(fig, "pendule.mp4",
                       300):  # on choisit la figure à animer, le nom du fichier à sauvegarder et la résolution en dpi
        for i in range(10):
            x0 = X[i]  # le point prend la valeur de X toutes les secondes
            y0 = Y[i]  # le point prend la valeur de Y toutes les secondes
            liste_X.append(X[i])  # on remplit toutes les secondes la liste vide avec les valeurs de X
            liste_Y.append(Y[i])  # on remplit toutes les secondes la liste vide avec les valeurs de Y
            red_dot.set_data(x0, y0)  # set.data attribue les valeurs chaque seconde
            courbe.set_data(liste_X, liste_Y)
            circle.set_data(c, d)
            triangle.set_data(f, g)
            writer.grab_frame()

    return X, Y


calculPeriode()
graph_pendule()
startfile(
    "C:\\path\\to\\file")  # chemin jusqu'au fichier et l'ouvre automatiquement le fichier
