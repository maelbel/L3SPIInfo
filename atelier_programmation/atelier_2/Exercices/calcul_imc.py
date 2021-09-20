# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:54:05 2021

@author: maelb
"""

def message_imc(imc:float)-> str:
    """Fonction interpretant l'IMC d'une personne
    inputs:
        imc: float Représente l'imc de l'utilisateur
    outputs:
        str: message contenant l'état de santé de l'utilisateur"""    
    
    #CONSTANTES
    IMC_1 = 16.5
    IMC_2 = 18.5
    IMC_3 = 25
    IMC_4 = 30
    IMC_5 = 35
    IMC_6 = 40    
    
    #Si l'IMC de la personne est inférieur à 16.5
    if imc < IMC_1:
        #On enregistre son état
        interpretation = "Dénutrition ou famine"
    #Si l'IMC de la personne est inférieur ou égale à 18.5
    elif imc <= IMC_2:
        #On enregistre son état
        interpretation = "Maigreur"
    #Si l'IMC de la personne est inférieur ou égale à 25    
    elif imc <= IMC_3:
        #On enregistre son état
        interpretation = "Corpulence normale"
    #Si l'IMC de la personne est inférieur ou égale à 30    
    elif imc <= IMC_4:
        #On enregistre son état
        interpretation = "Surpoids"
    #Si l'IMC de la personne est inférieur ou égale à 35    
    elif imc <= IMC_5:
        #On enregistre son état
        interpretation = "Obésité modéré"
    #Si l'IMC de la personne est inférieur ou égale à 40    
    elif imc <= IMC_6:
        #On enregistre son état
        interpretation = "Obésité sévère"    
    else:
        #Sinon on enregistre son état
        interpretation = "Obésité morbide"
    
    return interpretation

def test()-> None:
    """Procédure de test
    outputs: None"""
    
    #Variables saisi
    imc1 = float(input("Saisir l'IMC de la personne 1: "))
    imc2 = float(input("Saisir l'IMC de la personne 2: "))
    imc3 = float(input("Saisir l'IMC de la personne 3: "))
    
    #Appel de la fonction message_imc pour connaitre le niveau de santé de la personne
    print(message_imc(imc1))
    print(message_imc(imc2))
    print(message_imc(imc3))
    
test()