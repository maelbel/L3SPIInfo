# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:15:07 2021

@author: maelb
"""
def assurance_automobile()-> str:
    """Fonction qui retourne le tarif d'assurance automobile
    outputs:
        str: Retourne un message contenant le tarif pour l'utilisateur"""
    
    #Variables
    age = int(input("Veuillez saisir votre âge: "))
    permis = int(input("Veuillez saisir depuis combien de temps avez vous votre permis: "))
    nb_accident = int(input("Combien d'accident avez-vous eu ? \n"))
    temps_assurance = int(input("Depuis combien de temps êtes-vous dans l'assurance: "))
    
    tarif = ""
    
    #CONSTANTES
    AGE_25 = 25
    PERMIS = 2
    ACCIDENT_0 = 0
    ACCIDENT_1 = 1
    ACCIDENT_2 = 2
    TARIF_BLEU = "Tarif bleue"
    TARIF_VERT = "Tarif vert"
    TARIF_ORANGE = "Tarif orange"
    TARIF_ROUGE = "Tarif rouge"
    PAS_TARIF = "Vous ne pouvez pas être assurer chez nous"
    TEMPS_ASSURANCE_1 = 1
    
    if age < AGE_25:
        if permis < PERMIS:
            if nb_accident == ACCIDENT_0:
                tarif = TARIF_ROUGE
            else:
                tarif = PAS_TARIF
        else:
            if nb_accident == ACCIDENT_0:
                tarif = TARIF_ORANGE
            else:
                tarif = PAS_TARIF
    
    else:
        if permis < PERMIS:
            if nb_accident == ACCIDENT_0:
                tarif = TARIF_ORANGE
            elif nb_accident == ACCIDENT_1:
                tarif = TARIF_ROUGE
            else:
                tarif = PAS_TARIF
        else:
            if nb_accident == ACCIDENT_0:
                tarif = TARIF_VERT
            elif nb_accident == ACCIDENT_1:
                tarif = TARIF_ORANGE
            elif nb_accident == ACCIDENT_2:
                tarif = TARIF_ROUGE
            else:
                tarif = PAS_TARIF
    
    if temps_assurance >= TEMPS_ASSURANCE_1:
        if tarif == TARIF_VERT:
            tarif = TARIF_BLEU
        elif tarif == TARIF_ORANGE:
            tarif = TARIF_VERT
        elif tarif == TARIF_ROUGE:
            tarif = TARIF_ORANGE
            
    return tarif

print(assurance_automobile())