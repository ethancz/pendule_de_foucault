import matplotlib.pyplot as plt
from math import *
import numpy as np

g = 9.81
l = 67
w = sqrt(g / l)
X0 = 1
Omega = (2 * pi) / 86164  # vitesse de rotation de la terre en rad/s
t = np.linspace(0, 100, 1)
lambdaa = 48

X = X0 * cos(w * t)
Y = (X0 * Omega * sin(lambdaa) * sin(w * t)) / w

plt.figure(1)
plt.plot(t, X, Y)
plt.show()
