# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:56:54 2021

@author: maelb
"""

def impots()-> str:
    """Fonction pour savoir si une personne est imposable ou non
    outputs:
        str: message si l'utilisateur est imposable ou non"""
    
    #Variables
    #On met dans une variable le genre de la personne
    genre = input("Veuillez saisir votre genre (H ou F): ")
    #On met dans une variable son age
    age = int(input("Veuillez saisir votre âge: "))
    
    #Constantes
    AGE_18 = 18
    AGE_20 = 20
    AGE_35 = 35
    
    #Si c'est un homme et qu'il a 20 ans ou plus 
    if genre == 'H' and age >= AGE_20:
        #On affiche qu'il est imposable
        message = "Vous etes imposable"
    #Sinon si c'est une femme et qu'elle a 18 ans ou plus
    elif genre == 'F' and age >= AGE_18:
        #Si elle est a moins de 35 ans
        if age <= AGE_35:
            #On affiche qu'elle est imposable
            message = "Vous etes imposable"
        else:
            #Sinon on affiche qu'elle n'est pas imposable
            message = "Vous n'etes pas imposable"
    else:
        #On affiche que lui n'est pas imposable
        message = "Vous n'etes pas imposable"

    return message

#On lance la fonction
print(impots())