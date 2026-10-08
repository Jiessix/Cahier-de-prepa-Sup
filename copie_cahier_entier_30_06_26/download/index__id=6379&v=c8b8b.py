# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# definition d'une fonction
#tu dois cliquer sur la flèche verte 
def f(x):
    return x+1
# return interrompt une fonction

def g(x):
    print(2*x)
    
    
    #%%  Déclaration des variables globales   

import numpy as np
import matplotlib.pyplot as plt

t0 = 0
t1 = 3
T = 0.001
lbd = 0.5
u0 = 0
n = 1000
R = 100e3
C = 1e-6
E0 = 1
tau = R*C

#%%  Question 1   Création de la fonction créneau temporel
def creneau(t):
    if t%T < lbd*T:  
        return E0
    else:
        return 0

#%%  Question 2    Définition de la fonction f à utiliser dans l'itération
def f(u,t):
    return -u/tau+creneau(t)/tau

#%%  Question     Mise en oeuvre de la méthode d'Euler
def euler(f,u0,t,n):
    h = t[1]-t[0]
    u = np.zeros(n)
    u[0] = u0
    for i in range(n-1):
        u[i+1] = u[i]+h*f(u[i],t[i])
    return u

#%%  Question 4    Définition du tableau des temps , tracé du créneau, tracé de u_c
t = np.linspace(t0,t1,n)
u = euler(f,u0,t,n)
e = np.array([creneau(temps) for temps in t])

plt.close('all')
plt.figure()
plt.plot(t,e, '--r', label = 'e(t)')
plt.plot(t,u,'-b',  label = 'u(t)')
plt.xlabel('t (ms)')
plt.ylabel('e, u (V)')
plt.legend()


#%%  Question 6   Calcul de la dérivée de la tension u_c
def diff(f,t):
    ff = np.zeros(len(f)-1)
    for i in range(len(f)-1):
        ff[i] = (f[i+1]-f[i])/(t[i+1]-t[i])
    return ff

#%%  Question 7,8   Tracé de l'intensité et de la tension au cours du temps
    
i = C*diff(u,t)
tt = np.linspace(t0,t1,n-1)

plt.close('all')
figure, axis = plt.subplots(1, 2)
axis[0].plot(t, u)
axis[0].plot(t, e)
axis[0].set_title("u")
  
axis[1].plot(tt, i)
#axis[1].plot(t, e)
axis[1].set_title("i")


#%%  Question 9    Energie stockée dans le condensateur
Ec = C*u**2/2

plt.close('all')
plt.plot(t,Ec)
plt.xlabel('t (s)')
plt.ylabel('E (Joules)')


#%%  Question 10   Puissance instantanée dissipée par effet Joule
Pr = R*i**2

plt.close('all')
plt.plot(tt,Pr)
plt.xlabel('t (s)')
plt.ylabel('Pr (Watts)')

#%%  Question 11  Dérivée de l'énergie stockée
dEc = diff(Ec,t)

plt.close('all')
plt.plot(tt,dEc)
plt.xlabel('t (s)')
plt.ylabel('dEc/dt (Watts)')

#%%  Question 12
ee = np.array([creneau(temps) for temps in tt])
Prc = Pr+dEc
Pgen = ee*i
Ptot = Prc-Pgen

plt.close('all')
plt.plot(tt,Prc, label = 'R+C')
#%%plt.plot(tt,Pgen, label = 'gen')
#%% plt.plot(tt,Ptot, label = 'tot')
plt.xlabel('t (s)')
plt.ylabel('Pr+dEc/dt (Watts)')
plt.legend()




