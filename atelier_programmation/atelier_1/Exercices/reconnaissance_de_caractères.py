# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:30:11 2021

@author: maelb
"""

def reconnaissance_de_caractère()-> str:
    '''Fonction pour determiné le type de caractère saisie
    outputs:
        str: Retourne le type du caractère saisie'''
    
    #Variables
    #On demande à l'utilisateur de rentrer un caractère dans la console et on enregistre ce caractère dans une variable
    car = input("Entrez un caractère : ")
    
    #Si le caractère est contenue entre a et z
    if car>='a' and car<='z':
        #Alors on affiche que c'est une lettre minuscule
        message = "C'est une lettre minuscule"
    #Sinon si le caractère est contenue entre A et Z
    elif car>='A' and car<='Z':
        #Alors on affiche que c'est une lettre majuscule
        message = "C'est une lettre majuscule"
    #Sinon si le caractère est entre 1 et 9
    elif car>='1' and car<='9':
        #Alors on affiche que c'est un chiffre
        message = "C'est un chiffre"
    else: 
        #Sinon on affiche que c'est un caractère spécial
        message = "C'est un caractère spécial"
        
    return message

#On lance la fonction
print(reconnaissance_de_caractère())