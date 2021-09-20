# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:06:20 2021

@author: maelb
"""
import random

def choose_elt_list(list_in_which_to_choose:[int])-> int:
    """Fonction qui retourne un élément random de la liste
    inputs:
        list_in_which_to_choose: [int] Représente une liste d'entier
    outputs:
        int: Représente l'entier aléatoire à retourner"""

    #Variables
    taille_l = len(list_in_which_to_choose)
    i_rand = random.randint(0,taille_l-1) #Choisi un indice random compris entre 0 et taille_l

    #On enregistre l'élément aléatoire de la liste dans une variable
    int_random = list_in_which_to_choose[i_rand]

    return int_random

def test_choose_elt_list()-> None:
    """Procédure de test
    outputs: None"""
    # Test de votre code
    lst_sorted = [i for i in range(10)]
    print('Liste triée de départ',lst_sorted)
    e1 = choose_elt_list(lst_sorted)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = choose_elt_list(lst_sorted)
    while e1 == e2:
        e2 = choose_elt_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"

test_choose_elt_list()
