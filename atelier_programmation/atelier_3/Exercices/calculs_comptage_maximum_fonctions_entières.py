# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:36:44 2021

@author: maelb
"""

def somme_1(lst:list)-> int:
    """Fonction pour calculer la somme des valeurs d'une liste
    inputs:
        lst: list Liste comprenant des valeurs
    outputs:
        somme: float Retourne la somme des valeurs d'une liste"""
    
    #Variables
    somme = 0
    taille_l = len(lst)
    
    #Pour tous les éléments de la liste
    for i in range(taille_l):
        #On ajoute à la somme l'élément i de la liste l
        somme+=lst[i]
    
    return somme

def somme_2(lst:list)-> int:
    """Fonction pour calculer la somme des valeurs d'une liste
    inputs:
        lst: list Liste comprenant des valeurs
    outputs:
        somme: float Retourne la somme des valeurs d'une liste"""
    
    #Variables
    somme = 0
    
    #Pour tous les éléments de la liste l
    for element in lst:
        #On ajoute à la somme l'élément e de l'indice i de la liste l
        somme += element
    
    return somme

def somme_3(lst:list)-> int:
    """Fonction pour calculer la somme des valeurs d'une liste
    inputs:
        lst: list Liste comprenant des valeurs
    outputs:
        somme: float Retourne la somme des valeurs d'une liste"""
    
    #Variables
    somme = 0
    taille_l = len(lst)
    cpt = 0
    
    #Tant que le compteur est différent de la taille de la liste l
    while cpt != taille_l:
        #On ajoute à la somme l'élément numéro cpt de la liste l
        #Donc, pour la première execution de la boucle: l[0]
        somme+=lst[cpt]
        #Et on ajoute 1 au compteur
        cpt+=1
    
    return somme

def test_somme()-> None:
    """Procédure test pour afficher la somme
    outputs: None"""
    print(somme_1([1,2,3,4,5,6,7,8,9]))
    print(somme_2([1,2,3,4,5,6,7,8,9]))
    print(somme_3([1,2,3,4,5,6,7,8,9]))
    
test_somme()

def test_exercice1()-> None:
    """Procédure test
    outputs: None"""
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme_2([]))
    #test somme 11111
    lst=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme_2(lst))

test_exercice1()

def moyenne(lst:list)-> float:
    """Fonction qui retourne la moyenne d'une liste
    inputs:
        lst: list Liste comprenant des valeurs
    outputs:
        moyenne_lst: float Moyenne des valeurs de la liste"""
    
    #Variables
    somme = 0
    moyenne_lst = 0.0
    taille_l = len(lst)
    
    #Si la liste est vide
    if lst == []:
        moyenne_lst = 0.0
    else:
        #Pour tous les éléments de la liste 
        for i in range(taille_l):
            #On ajoute à la somme l'élément i de la liste l
            somme+=lst[i]
    
        #On calcule la moyenne
        moyenne_lst = somme / taille_l
    
    return moyenne_lst

def test_moyenne()-> None:
    """Procédure test pour afficher la moyenne
    outputs: None"""
    print (moyenne([1,2,3,4,5,6,7,8,9]))
    
test_moyenne()

def nb_sup(lst:list, elt:int)-> list:
    """Fonction pour retourner tous les éléments supérieur à e de la liste l
    intputs:
        lst: list Liste d'éléments 
        elt: int Entier utilisé pour minorer les élément à afficher d'une liste
    outputs: 
        list: Retourne une liste de valeur supérieur à e"""
        
    #Variables
    taille_l = len(lst)
    compteur_elt_sup = 0
    
    #Pour les éléments i dans liste l
    for i in range(taille_l):
        #Si l'élément i est supérieur à e
        if lst[i] > elt:
            #On ajoute cet élément a la liste supérieur
            compteur_elt_sup += 1

    return compteur_elt_sup

def nb_sup_e(lst:list, elt:int)-> list:
    """Fonction pour retourner tous les éléments supérieur à e de la liste l
    intputs:
        lst: list Liste d'éléments 
        elt: int Entier utilisé pour minorer les élément à afficher d'une liste
    outputs: 
        list: Retourne une liste de valeur supérieur à e"""
        
    #Variables
    compteur_elt_sup = 0
    
    #Pour les éléments dans la liste l
    for element in lst:
        #Si l'élément e de la liste est supérieur à l'élément e
        #du paramètre formel de la fonction 
        if element > elt:
            #On ajoute cette valeur a la liste
            compteur_elt_sup += 1

    return compteur_elt_sup


def test_nb_sup()-> None:
    """Procédure pour afficher les nombres supérieur à un élément
    outputs: None"""
    
    print(nb_sup_e([1,2,3,4,5,6,7,8,9], 5))
    
test_nb_sup()

def moyenne_sup(lst:list, elt:int)-> list: 
    """Fonction pour retourner tous les éléments supérieur à e de la liste l
    intputs:
        lst: list Liste d'éléments 
        elt: int Entier utilisé pour minorer les élément à afficher d'une liste
    outputs: 
        list: Retourne la moyenne des valeurs supérieur à e"""
        
    #Variables
    taille_l = len(lst)
    superieur = []
        
    #Pour les éléments i dans liste l
    for i in range(taille_l):
        #Si l'élément i est supérieur à e
        if lst[i] > elt:
            #On ajoute cet élément a la liste superieur
            superieur.append(lst[i])
    
    return moyenne(superieur)

def test_moyenne_sup()-> None:
    """Procédure pour afficher la moyenne des éléments supérieur d'une liste à un élément e
    outputs: None"""
    
    print(moyenne_sup([1,2,3,4,5,6,7,8,9], 5))

test_moyenne_sup()

def val_max(lst:list)-> int:
    """Fonction pour retourner la valeur max d'une liste
    inputs:
        lst: list Liste d'éléments
    outputs: 
        list: Retourne la valeur maximal d'une liste d'éléments"""
    
    #Variables
    taille_l = len(lst)
    v_max = 0
    
    #Pour tous les elements de la liste l
    for i in range(taille_l):
        #Si l'élément i de la liste est supérieur à la valeur maximum
        if lst[i] > v_max:
            #On remplace la valeur max
            v_max = lst[i]
    
    return v_max

def ind_max(lst:list)-> int:
    """Fonction pour retourner l'indice de la valeur max d'une liste
    inputs:
        lst: list Liste d'éléments
    outputs: 
        list: Retourne l'indice de la valeur maximal d'une liste d'éléments"""
    
    #Variables
    taille_l = len(lst)
    v_max = 0
    
    #Pour tous les elements de la liste l
    for i in range(taille_l):
        #Si l'élément i de la liste est supérieur à la valeur maximum
        if lst[i] > v_max:
            #On remplace la valeur max
            v_max = lst[i]
            i_max = i
    
    return i_max
