# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:05:56 2021

@author: maelb
"""
#Importer toutes les fonctions du module pyhton random
import random

def gen_list_random_int(int_binf = 0, int_bsup = 10)-> [int]:
    """Fonction qui retourne une liste de nombre aléatoire
    inputs:
        int_binf: int Représente un entier
        int_bsup: int Représente un entier
    outputs:
        [int]: Représente une liste de nombre aléatoire"""

    #Variables
    int_nbr = []
    compteur = 0

    #Tant que le compteur est inférieur à l'entier supérieur
    while compteur < int_bsup:
        #On ajoute à la liste int_nbr un nombre aléatoire
        #compris entre int_binf (inclus) et int_bsup (exclus)
        int_nbr.append(random.randrange(int_binf, int_bsup))
        compteur += 1
    return int_nbr

print(gen_list_random_int())
