# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:43:50 2021

@author: maelb
"""
import random

def mix_list(list_to_mix:[int])-> [int]:
    """Fonction qui retourne une liste mélangée
    inputs:
        list_to_mix: [int] Représente une liste potentiellement triée
    outputs:
        [int]: Représente une liste mélangée"""
        
    #Variables
    mixed_list = []
    taille_l = len(list_to_mix)
    #Pour tous les éléments i de la liste
    for i in range(taille_l):
        int_to_mix = list_to_mix[i]
        i_rand = random.randint(0,taille_l)
        mixed_list.insert(i_rand, int_to_mix)
    
    return mixed_list

def test_mix_list()-> None:
    """Procédure de test
    outputs: None"""
    # Test de votre code
    lst_sorted = [i for i in range(10)]
    print('Liste triée de départ',lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print('Liste mélangée obtenue',mixed_list)
    print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted)
    #assert (cf. doc en ligne) permet de vérifier qu’une condition
    #est vérifiée en mode debug (désactivable)
    assert lst_sorted != mixed_list,"Les deux listes doivent être différente après l'appel à mixList..."

#test_mix_list()