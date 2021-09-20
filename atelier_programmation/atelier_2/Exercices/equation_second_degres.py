# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:45:19 2021

@author: maelb
"""
from math import sqrt

def discriminant(a:float, b:float, c:float)-> float:
    """Fonction pour calculer le discriminant d'une équation
    inputs:
        a: float Représente la valeur a pour calculer le discriminant
        b: float Représente la valeur b pour calculer le discriminant
        c: float Représente la valeur c pour calculer le discriminant
    outputs:
        float: Renvoie le discriminant"""
        
    return b**2 - 4*a*c

def racine_unique(a:float, b:float)-> float:
    """Fonction calculer la racine unique d'une équation
    inputs:
        a: float Représente la valeur a pour calculer la racine
        b: float Représente la valeur b pour calculer la racine
    outputs:
        float: Renvoie la racine de l'équation"""
        
    return (-b)/(2*a)

def racine_double(a:float, b:float, delta:float, num:int)-> float:
    """Fonction pour calculer les deux racines d'une équation
    inputs:
        a: float Représente la valeur a pour calculer les deux racines
        b: float Représente la valeur b pour calculer les deux racines
        delta: float Représente la valeur delta (discriminant) pour calculer les deux racines
        num: int Représente la valeur pour calculer la première racine ou la deuxième
    outputs:
        float: Renvoie l'une des deux racines de l'équation"""
    
    #Variables
    resultat = 0.0
    
    #Si c'est la première racine
    if num == 1:
        #On la calcule
        resultat = (-b+sqrt(delta))/(2*a)
    #Si c'est la deuxième racine
    if num == 2:
        #On la calcule
        resultat = (-b-sqrt(delta))/(2*a)
        
    return resultat
    
def str_equation(a:float, b:float, c:float)-> str:
    """Fonction pour afficher l'équation en string
    inputs:
        a: float Représente la valeur a de l'équation
        b: float Représente la valeur b de l'équation
        c: float Représente la valeur c de l'équation
    outputs:
        str: Renvoie l'équation sous forme d'une chaine de caractère"""
    
    #Variables
    astr = 'x2'
    bstr =  'x'
    signb = '+'
    signc = '+'
    
    #On enlève les éléments inutiles
    #Pour a
    if a == -1:
        a = '-'
    elif a == 0:
        astr=''
        a = ''
        signb = ''
    elif a == 1:
        a = ''

    #Pour b
    if b<0:
        signb= ''
    elif b == -1:
        b = '-'
    elif b == 0:
        bstr = ''
        b = ''
        signb = ''
    elif b == 1:
        b = ''

    #Pour c
    if c<0:
        signc = ''
    elif c == 0:
        c = ''
        signc = ''  

    message = str(a)+astr+signb+str(b)+bstr+signc+str(c)+"=0"
    return message


def solution_equation(a:float, b:float, c:float)-> str:
    """Fonction pour afficher la solution de l'équation
    inputs:
        a: float Représente la valeur a de l'équation
        b: float Représente la valeur b de l'équation
        c: float Représente la valeur c de l'équation
    outputs:
        str: Renvoie la solution de l'équation sous forme d'une chaine de caractère"""
    
    #Variables
    delta = discriminant(a, b, c)
    
    #Si delta est négatif
    if delta < 0:
        #On crée le message contenant la solution de l'équation
        message = "Solution de l'équation "+str(str_equation(a, b, c))+"\nPas de racine réelle\n\n"
    #Si delta est égale à 0
    elif delta == 0:
        #On crée le message contenant la solution de l'équation
        message = "Solution de l'équation "+str(str_equation(a, b, c))+" \nRacine unique : x="+str(racine_unique(a, b))+"\n\n"
    else:
        #Sinon on crée le message contenant la solution de l'équation
        message = "Solution de l'équation "+str(str_equation(a, b, c))+" \nDeux racines : \nx1="+str(racine_double(a, b, delta, 1))+" \nx2="+str(racine_double(a, b, delta, 2))+"\n\n"

    return message

def equation(a:int, b:int, c:int)-> str:
    """Fonction pour afficher le résultat de l'équation
    inputs:
        a: int Représente la valeur a de l'équation
        b: int Représente la valeur b de l'équation
        c: int Représente la valeur c de l'équation
    outputs:
        str: Affiche le message de la solution de l'équation"""
    return print(solution_equation(a, b, c))

def test()-> None:
    """Procédure de test
    outputs: None"""
    
    equation(1, 2, 3)
    equation(0, 1, -1)
    equation(1, 0, 1)
    equation(1, 2, 0)
    
test()