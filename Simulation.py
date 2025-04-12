#=================================================================================================================
# PARTIE 1: APPELS DES FICHERS ET LIBRARIES EXTERNE (IMPORT)
#=================================================================================================================

import math
import matplotlib.pyplot as plt

# ==============================================================================
# PARTIE 2: DÉFINITION DES FONCTIONS
# ==============================================================================
# ==============================================================================

def z(Z0, ms, k, V0z, K, t):
    return Z0 + (ms / k) * (V0z - K) * (1 - math.exp(-k / ms * t)) + K * t


def x(X0, ms, k, v0x, t):
    return X0 + (ms / k) * v0x * (1 - math.exp(-k / ms * t))



def Affichage(i, xmin, xmax, xm):
    if i == 0:
        print(f"{'i':^5s}  {'temps':^12.5s}  {'x(t)':^12.5s}  {'z(t)':^12.5s}")
    print(f"{i:5d}  {xmin:12.5e}  {xm:12.5e}  {xmax:12.5e}")


def recherche_zero(xmin, xmax, epsilon):
    global xm
    while abs(xmax) - abs(xmin) > epsilon:
        xm = (xmin + xmax) / 2
        fxmin = z(Z0, ms, k, v0z, K, xmin)
        fxm = z(Z0, ms, k, v0z, K, xm)

        if fxmin * fxm > 0:
            xmin = xm
        else:
            xmax = xm
    return xm

# ==============================================================================
# PARTIE 3: CORPS PRINCIPAL DU SCRIPT (MAIN)
# ==============================================================================
# ==============================================================================

# toute les varibles

V0 = 22.0  # Vitesse initiale en m/s
O0 = math.radians(45)  # Angle de tir en degrés (converti en radians)
Z0 = 10.0  # Hauteur initiale en m
x0 = 0.0  # Avancée initiale en m
ms = 1.0  # Masse solide en kg
Ps = 1.0  # Masse volumique solide en kg/L
Pf = 1.3e-3  # Masse volumique du liquide en kg/L
k = 1.0  # Coefficient de frottement en kg/s
g = 9.81  # Force de pesanteur en m/s^2
epsilon = 1e-9  # Précision du code
mf = (ms / Ps) * Pf  # Masse du fluide
K = -(ms / k) * (1 - (mf / ms)) * g
v0z = abs(V0) * math.sin(O0)
v0x = abs(V0) * math.cos(O0)
xmin = 0.0
xmax = 0.0
i = 0
xm = 0
AS = 0
m =0
x1 = []
z1 = []
t1 = []


#recherche borne xmax
while AS == 0:
    fxmax = z(Z0, ms, k, v0z, K, xmax)
    if fxmax >= 0:
        xmax += 1
        print(f"La borne xmax est fixée à ", xmax, " seconde")
    else:
        AS = 1

t = recherche_zero(xmin, xmax, epsilon)
#impresion du tableau

while i < 100:

    xt = x(x0, ms, k, v0z, t/100*i)
    zt = z(Z0, ms, k, v0z, K, t/100*i)
    Affichage(i, t/100*i, xt, zt)
    i += 1

xt = x(x0, ms, k, v0z, t)
zt = z(Z0, ms, k, v0z, K, t)
Affichage(i, t, xt, zt)



#impresion du resulat aprosche
print("")
print("Le projectile tombe à", t, " seconde")

# ==============================================================================
# PARTIE 4: BONUS Grapher le tout
# ==============================================================================
# ==============================================================================

while m < 100:
    x1.append(x(x0, ms, k, v0z, t/100*m))
    z1.append((z(Z0, ms, k, v0z, K, t/100*m)))
    t1.append(t/100*m)
    m +=1

plt.plot(t1, x1)
plt.title('t en fonction de x (distance en fonction du temps)  ')
plt.xlabel('temps en seconde (s)')
plt.ylabel('distance en M')
plt.show()

plt.plot(t1, z1)
plt.title('t en fonction de z (hautuer en fonction du temps)')
plt.xlabel('temps en seconde (s)')
plt.ylabel('hautuer en M')
plt.show()

plt.plot(x1, z1)
plt.title('x en fonction de z (distance parcourus trajectroire du projectile)')
plt.xlabel('distance en M')
plt.ylabel('hautuer en M')
plt.show()

