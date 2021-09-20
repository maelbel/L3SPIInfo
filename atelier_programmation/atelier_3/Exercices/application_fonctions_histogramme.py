# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 08:49:40 2021

@author: maelb
"""
import matplotlib.pyplot as plt
from calculs_comptage_maximum_fonctions_entières import val_max

#QUESTION 1
def histo(freq:[int])-> [int]:
    """Fonction qui retourne la liste d'entier histo
    inputs:
        freq: [int] Représente une liste d'entier'
    outputs:
        [int]: Retourne une liste d'entier'
        """
    
    #Variables
    taille_l = len(freq)
    v_max = 0
    histo = []
    
    #Pour tous les elements de la liste l
    for i in range(taille_l):
        #Si l'élément i de la liste est supérieur à la valeur maximum
        if freq[i] > v_max:
            #On remplace la valeur max
            v_max = freq[i]
    
    #Initialisation de la liste histo à 0
    for i in range(v_max+1):
        histo.append(0)
    
    #Pour toutes les valeurs dans la liste freq
    for i in range(taille_l):
        #On récupère la valeur i dans la liste freq 
        val = freq[i]
        #Et on ajoute 1 dans la liste dont l'index est egale à la valeur
        histo[val] += 1 
    
    return histo

def test_histo()-> None:
    """Procédure de test
    outputs: None"""
    
    print(histo([5,5,5,3,2,1,9,4,6]))
    print(histo([0,1,2,3,4,5,6,7,8,9]))
    print(histo([0,3,2,1,9,4,6]))
    
test_histo()

def est_injective(freq:list)-> bool:
    """Fonction qui retourne True si la liste est injective ou False si elle ne l'est pas
    inputs:
        freq: [int]
    outputs:
        boolean: True si la liste est injective ou False si elle ne l'est pas"""
    
    #Variables
    injective = True
    histogramme = histo(freq)
    taille_l = len(histogramme)
    compteur = 0
    
    #Tant que injective est vrai et le compteur inf à la taille de histogramme
    while injective and compteur < taille_l:
        #Si la valeur de l'histo est supérieur à 1
        if histogramme[compteur] > 1:
            #L'histo n'est pas injective
            injective = False
        compteur += 1
        
    return injective

def test_est_injective()-> None:
    """Procédure de test
    outputs: None"""
    
    print(est_injective([5,5,5,3,2,1,9,4,6]))
    print(est_injective([0,1,2,3,4,5,6,7,8,9]))
    print(est_injective([0,3,2,1,9,4,6]))
    
test_est_injective()

def est_surjective(freq:list)-> bool:
    """Fonction qui retourne True si la liste est surjective ou False si elle ne l'est pas
    inputs:
        freq: [int] Représente une liste d'entier'
    outputs:
        boolean: True si la liste est surjective ou False si elle ne l'est pas"""
    
    #Variables
    surjective = True
    histogramme = histo(freq)
    taille_l = len(histogramme)
    compteur = 0
    
    #Tant que surjective est vrai et le compteur inf à la taille de histogramme
    while surjective and compteur < taille_l:
        #Si la valeur de l'histo est égale à 0
        if histogramme[compteur] == 0:
            #L'histo n'est pas surjective
            surjective = False
        compteur += 1
        
    return surjective

def test_est_surjective()-> None:
    """Procédure de test
    outputs: None"""
    
    print(est_surjective([5,5,5,3,2,1,9,4,6]))
    print(est_surjective([0,1,2,3,4,5,6,7,8,9]))
    print(est_surjective([0,3,2,1,9,4,6]))
    
test_est_surjective()

def est_bijective(freq:list)-> bool:
    """Fonction qui retourne True si la liste est bijective ou False si elle ne l'est pas
    inputs:
        freq: [int] Représente une liste d'entier'
    outputs:
        boolean: True si la liste est bijective ou False si elle ne l'est pas"""
    
    return est_injective(freq) and est_surjective(freq)

def test_est_bijective()-> None:
    """Procédure de test
    outputs: None"""
    
    print(est_bijective([5,5,5,3,2,1,9,4,6]))
    print(est_bijective([0,1,2,3,4,5,6,7,8,9]))
    print(est_bijective([0,3,2,1,9,4,6]))
    
test_est_bijective()

#QUESTION 2
def affiche_histo(freq:[int])-> str:
    """Fonction pour afficher un histogramme
    intputs:
        freq: [int] Représente une liste d'entier
    outputs:
        str: Représente l'histogramme"""
    histogramme = histo(freq)
    MAXOCC = val_max(histogramme)
    
    