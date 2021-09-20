# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:25:03 2021

@author: maelb
"""

def elections_legislatives():
    '''Fonction qui retourne le résultat des elections pour le premier candidat
    outputs:
        string: Chaine de caractère contenant si le premier candidat est gagnant, perdant, favorable ou défavorable'''
        
    #Variables
    score = [0, 1, 2, 3]
    taille_score = len(score)
    premier = True
    
    for i in range(taille_score):
        score[i] = float(input("Veuillez saisir le score du candidat "+ str(i+1)+" : "))
    
    #CONSTANTES
    POURCENTAGE_50 = 50
    POURCENTAGE_12_DEMI = 12.5
    POURCENTAGE_CANDIDAT1 = score[0]
    
    for i in range(1, taille_score):
        if score[i]>=50:
            message = "Le candidat numéro 1 n'a pas gagné les élections législatives"
            premier = False
    
    if POURCENTAGE_CANDIDAT1 >= POURCENTAGE_50:
        message = "Le candidat numéro 1 à gagné les élections législatives"
    elif POURCENTAGE_CANDIDAT1 < POURCENTAGE_12_DEMI:
        message = "Le candidat numéro 1 n'a pas gagné les élections législatives"
    else:
        for i in range(taille_score):
            if premier:
                if POURCENTAGE_CANDIDAT1 > score[i]:
                    premier = True
                else:
                    premier = False
        if premier:
            message = "Le candidat numéro 1 se retrouve en ballottage favorable pour le second tour des élections législatives"
        else:
            message = "Le candidat numéro 1 se retrouve en ballottage défavorable pour le second tour des élections législatives"
    
    return message

print(elections_legislatives())