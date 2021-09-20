# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:20:04 2021

@author: maelb
"""
import random

def extract_elements_list(list_in_which_to_choose:[int], int_nbr_of_elt_to_extract:int)-> [int]:
    """Fonction qui retourne un nombre d'entier aléatoire d'une liste
    inputs:
        list_in_which_to_choose: [int] Représente une liste d'entier
        int_nbr_of_element_to_extract: int Représente un entier
    outputs:
        [int]: Retourne une liste de int_nbr_of_elt_to_extract élément(s)"""
    #Variables
    taille_l = len(list_in_which_to_choose)-1
    lst_int = []
    compteur = 0
    
    #Tant que le compteur est inférieur au nombre d'éléments à extraire
    while compteur < int_nbr_of_elt_to_extract:
        #On récupère un indice aléatoire
        i_rand = random.randint(0, taille_l)
        #On ajoute à la liste list_int un élément 
        #de la liste list_in_which_to_choose aléatoire
        lst_int.append(list_in_which_to_choose[i_rand])
        compteur += 1
    return lst_int
    
def test_extract_elements_list()-> None:
    """Procédure de test
    outputs: None"""
    # Test de votre code
    lst_sorted = [i for i in range(10)]
    print('Liste de départ',lst_sorted)
    sublist = extract_elements_list(lst_sorted,5)
    print('La sous liste extraite est',sublist)
    print('Liste de départ après appel de la fonction est',lst_sorted)
    
test_extract_elements_list()
