# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:58:56 2021

@author: maelb
"""

def salaire()-> float:
    '''Fonction pour calculer le salaire
    outputs:
        float: Retourne le salaire'''
    
    #Variables
    salaire_horaire= 8
    horaire_travail= 165
    
    #CONSTANTES
    VCINQ_POURCENT = 1+25/100
    CINQUANTE_POURCENT = 1+50/100
    
    #On calcule le salaire normal
    salaire = salaire_horaire*horaire_travail
    #Si l'horaire de travail est inférieur à 200 heures et supérieur ou égale à 160 heures
    if 200>horaire_travail and horaire_travail>=160:
        #On ajoute 25% du salaire au salaire initiale
        salaire=salaire+salaire*VCINQ_POURCENT
    #Sinon si l'horaire de travail est supérieur ou égale à 200 heures
    elif horaire_travail>=200:
        #On ajoute 50% du salaire au salaire initiale
        salaire=salaire+salaire*CINQUANTE_POURCENT
        
    #On retourne le salaire finale
    return salaire

#On lance la fonction
print(salaire())