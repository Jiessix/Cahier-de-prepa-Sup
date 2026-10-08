#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 23:15:03 2026

@author: marie-lysbeoutis
"""

"""
"""

# ============================================================
# 1) IMPORT DES MODULES
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ============================================================
# 2) DEFINITION DES SYSTEMES DIFFERENTIELS
# ============================================================

"""
On transforme l’équation d’ordre 2 en système d’ordre 1
en posant :

y0 = theta
y1 = theta'

Le vecteur est donc :
y = [theta, theta']

On doit alors définir :
y0' = y1
y1' = -omega0^2 sin(y0)     (modèle exact)
"""

def pendule_exact(y, t, omega0):
    """
    Modèle exact (non linéaire)
    """
    theta = y[0]
    theta_point = y[1]

    return [
        theta_point,
        -omega0**2 * np.sin(theta)
    ]


def pendule_linearise(y, t, omega0):
    """
    Modèle linéarisé (approximation petits angles)
    sin(theta) ≈ theta
    """
    theta = y[0]
    theta_point = y[1]

    return [
        theta_point,
        -omega0**2 * theta
    ]


# ============================================================
# 3) PARAMETRES DU PROBLEME
# ============================================================

omega0 = 2.0                     # pulsation propre
t = np.linspace(0, 10, 2000)     # intervalle de temps

# Angles initiaux à tester
angles_initiaux = [0.1, 0.5, 1.5]


# ============================================================
# 4) COMPARAISON TEMPORELLE
# ============================================================

plt.figure(figsize=(10, 6))

for theta0 in angles_initiaux:

    # condition initiale : vitesse initiale nulle
    y0 = [theta0, 0]

    # résolution numérique
    sol_exact = odeint(pendule_exact, y0, t, args=(omega0,))
    sol_lin = odeint(pendule_linearise, y0, t, args=(omega0,))

    # tracé
    plt.plot(t, sol_exact[:, 0], label=f"Exact θ0={theta0}")
    plt.plot(t, sol_lin[:, 0], "--", label=f"Linéarisé θ0={theta0}")

plt.xlabel("Temps")
plt.ylabel("Angle θ (rad)")
plt.title("Comparaison modèle exact / modèle linéarisé")
plt.legend()
plt.grid()


# ============================================================
# 5) PORTRAIT DE PHASE
# ============================================================

plt.figure(figsize=(8, 6))

for theta0 in angles_initiaux:

    y0 = [theta0, 0]

    sol_exact = odeint(pendule_exact, y0, t, args=(omega0,))
    sol_lin = odeint(pendule_linearise, y0, t, args=(omega0,))

    # portrait de phase : theta' en fonction de theta
    plt.plot(sol_exact[:, 0], sol_exact[:, 1])
    plt.plot(sol_lin[:, 0], sol_lin[:, 1], "--")

plt.xlabel("θ")
plt.ylabel("θ'")
plt.title("Portraits de phase : exact (plein) / linéarisé (pointillé)")
plt.grid()

plt.show()

