# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:23:17 2021

@author: maelb
"""

def est_bissextile(annee:int)-> bool:
    """Fonction qui renvoie True si l'année est bissextile
    inputs:
        annee: int représente l'année à tester
    outputs:
        boolean: True si l'annee est bissextile, False si elle ne l'est pas"""
    
    #CONSTANTES
    reste1 = annee%4
    reste2 = annee%100
    reste3 = annee%400
    
    return (reste1 == 0 and reste2 != 0) or reste3 == 0

def test()-> None:
    """Procédure de test
    outputs: None"""
    
    #Variables
    annee = int(input("Veuillez saisir une année: "))
    est = est_bissextile(annee)
    message = ""
    
    #Si l'année est bissextile
    if est:
        #On crée un message pour le dire
        message = "L'année " + str(annee) + " est une année bissextile"
    else:
        #Sinon on crée un message pour dire qu'elle ne l'est pas
        message = "L'année " + str(annee) + " n'est pas une année bissextile"
    
    print(message)
test()
