# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:58:19 2021

@author: maelb
"""
# Exemple d'utilisation
import time
#Pour mesurer le temps d'exécution nous avons à notre disposition
#la fonction perf_counter()
n = 10000000
#Récupération du temps système et démarrage du chronomètre
start_pc = time.perf_counter()
for i in range(n):
    #on ne fait rien…
    None
end_pc = time.perf_counter()
elapsed_time_pc = end_pc-start_pc
print("Temps écoulé entre les deux mesures : ",elapsed_time_pc)
print("Temps estimé pour une instruction",elapsed_time_pc/n)
# Exécutez ce code et vérifiez par vous-même la variabilité des mesures.

import matplotlib.pyplot as plt
import numpy as np
#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
x_axis_list = np.arange(0,5.5,0.5)
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de
#choisir éventuellement la couleur et le marqueur
ax.plot(x_axis_list,x_axis_list,'bo-',label='Identité')
ax.plot(x_axis_list,x_axis_list**2, 'r*-', label='Carré')
ax.plot(x_axis_list,x_axis_list**3,'g*-', label='Cube')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
title='Fonctions identité, cube et carré')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()

import random
import time
from melange_des_elements_d_une_liste import mixed_list

def perf_mix(mixed_list:callable, shuffle:callable, taille_liste: [int], nbr_execution:int)-> ([int],[int]):
    """Fonction qui retourne le temps d'execution moyen pour deux fonctions"""
    #Variables
    taille_l = len(taille_liste)
    somme = 0
    
    for n in taille_liste:
        start_pc = time.perf_counter()
        for i in range(n):
            #on ne fait rien…
            None
        end_pc = time.perf_counter()
        elapsed_time_pc = end_pc-start_pc
        somme += elapsed_time_pc
    moyenne = somme / taille_l

perf_mix()