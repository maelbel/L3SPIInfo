# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:00:26 2021

@author: maelb
"""

def position(lst: list, elt: int) -> int:
    """Fonction pour connaitre la position d'un élément dans une liste (boucle for)
    inputs:
        l: list Représente une liste d'élément
        e: int Représente un entier
    outputs:
        int: Retourne l'id de l'élément e s'il est présent dans la liste l, sinon retourne -1"""

    # Variables
    taille_l = len(lst)
    e_id = 0
    est_present = False

    #Pour tous les éléments d'une liste
    for i in range(taille_l):
        #Si l'élément e est égale a l'élément de la liste l
        if elt == lst[i]:
            #On dit qu'il est présent et enregistre son id
            est_present = True
            e_id = i
    
    #S'il n'est pas présent
    if not est_present:
        #On affecte -1
        e_id = -1
        
    return e_id

#print(position([1,2,3,4,5,6,7,8,9], 5))

def position2(lst:list, elt:int)-> int:
    """Fonction pour connaitre la position d'un élément dans une liste (boucle while)
    inputs:
        l: list Représente une liste d'élément
        e: int Représente un entier
    outputs:
        int: Rentourne l'id de l'élément e s'il est présent dans la liste l, sinon retourne -1"""
        
    # Variables
    taille_l = len(lst)
    e_id = 0
    est_present = False
    compteur = 0

    #Tant qu'il n'est pas présent et que le compteur est en-dessous de la taille du tableau
    #On sort de la boucle si l'un des deux est vrai
    while not est_present and compteur < taille_l:
        #Si l'élément e est égale a l'élément de la liste l
        if elt == lst[compteur]:
            #On dit qu'il est présent et enregistre son id
            est_present = True
            e_id = compteur
            
        compteur += 1
    
    #S'il n'est pas présent
    if not est_present:
        #On affecte -1
        e_id = -1
        
    return e_id

#print(position2([1,2,3,4,5,6,7,8,9], 5))

def nb_occurence(lst: list, elt: int) -> int:
    """Fonction pour connaitre le nombre de fois qu'un élément e apparait dans une liste
    inputs:
        l: list Représente une liste d'élément
        e: int Représente un entier
    outputs:
        e_id: int Rentourne le nombre d'élément e présent dans la liste l"""

    # Variables
    taille_l = len(lst)
    compteur_e = 0

    #Pour tous les éléments d'une liste
    for i in range(taille_l):
        #Si l'élément e est égale à l'élément i de la liste lst
        if elt == lst[i]:
            #On dit qu'il est présent et on ajoute 1 au compteur d'élément
            compteur_e += 1
        
    return compteur_e

#print(nb_occurence([1,2,3,4,5,6,5,7,5], 5))


def est_triee(lst:list)-> bool:
    """Fonction qui retourne si une liste est triee par ordre croissant ou non (boucle for)
    inputs:
        l: list Représente une liste d'élément qu'on va tester
    outputs:
        boolean: True si la liste est trié par ordre croissant, False si elle ne l'est pas"""
    
    #Variables
    taille_l = len(lst)
    sup = True
    
    #Pour tous les élément i de la liste lst
    for i in range(taille_l-1):
        #Si l'élément i de la liste lst est supérieur à l'élément suivant 
        if lst[i]>lst[i+1]:
            #La liste n'est pas triée
            sup = False
    
    return sup
        
#print(est_triee([1,2,3,4,5,6,5,7,5,6]))
#print(est_triee([1,2,3,4,5,6]))

def est_triee2(lst:list)-> bool:
    """Fonction qui retourne si une liste est triee par ordre croissant ou non (boucle while)
    inputs:
        l: list Représente une liste d'élément qu'on va tester
    outputs:
        boolean: True si la liste est trié par ordre croissant, False si elle ne l'est pas"""

    # Variables
    taille_l = len(lst)
    est_inferieur = True
    compteur = 0

    #Tant qu'il est inférieur et le compteur ne fait pas la taille de la liste
    while est_inferieur and compteur < taille_l-1:
        #Si l'élément de la liste est supérieur à l'élémént suivant
        if lst[compteur]>lst[compteur+1]:
            #La liste n'est pas triée
            est_inferieur = False
            
        compteur += 1
    
    return est_inferieur
    
#print(est_triee2([1,2,3,4,5,6,5,7,5,6,8,9,4,4,5,4,8,7,8]))
#print(est_triee2([1,2,3,4,5,6,7,8,9,10,11,12]))

def position_tri(lst:list, elt:int)-> int:
    """Fonction qui retourne la position d'un élément dans une liste (boucle for)
    inputs:
        l: list Représente une liste d'élément triée
        e: int Représente un entier
    outputs:
        int: Retourne l'id de l'élément e s'il est présent dans la liste l, sinon retourne -1"""
    #Variables
    taille_l = len(lst)-1
    e_id = 0
    est_present = False

    #Tant qu'il n'est pas présent et que l'id de l'élément est inférieur ou égale à la taille du tableau
    #On sort de la boucle si l'un des deux est vrai
    while not est_present and e_id <= taille_l:
        i_med = (e_id + taille_l) // 2
        #Si l'élément e est égale a l'élément de la liste l
        if elt == lst[i_med]:
            #On dit qu'il est présent et enregistre son id
            est_present = True
            e_id = i_med
        elif elt > lst[i_med]:
            e_id = i_med + 1
        else:
            taille_l = i_med - 1
            
    
    #S'il n'est pas présent
    if not est_present:
        #On affecte -1
        e_id = -1
        
    return e_id

#print(position_tri([0,1,2,3,4,5,6,7,8,9], 10))

def a_repetitions(lst:list)-> bool:
    """Fonction qui retourne le nombre de fois qu'un élément e est présent dans une liste l
    inputs:
        l: list Représente une liste qu'on va tester
        e: int Représente un entier qui va nous servir à tester la liste
    outputs:
        boolean: True si la liste L comporte des répétitions de valeurs et False sinon"""
    
    # Variables
    taille_l = len(lst)
    est_present = False
    compteur = 0
    pas_repeter = []

    #Pour tous les éléments d'une liste
    while not est_present and compteur < taille_l:
        if not lst[compteur] in pas_repeter:
            pas_repeter.append(lst[compteur])
        else:
            est_present = True
            
        compteur += 1
        
    return est_present

def test_a_repetitions()-> bool:
    """Procédure qui affiche la fonction a_répétitions
    outputs:
        boolean: Retourne True si le test est ..., sinon False"""
    
    #CONSTANTES
    LISTE_VIDE = []
    LISTE_UN_ELEMENT = [5]
    LISTE_NON_REPETEE = [1,2,3,4,5,6]
    LISTE_REPETEE_1 = [1,2,3,4,5,5]
    LISTE_REPETEE_2 = [1,1,3,4,5,6]
    LISTE_REPETEE_3 = [1,2,3,3,4,5]
    
    #Test: resultat attendu False
    print("Résultat attendu: False")
    #Test d'une liste vide
    print("Résultat obtenu pour la liste ", LISTE_VIDE, ": ", a_repetitions(LISTE_VIDE))
    #Test d'une liste avec un seul élément
    print("Résultat obtenu pour la liste ", LISTE_UN_ELEMENT, ": ", a_repetitions(LISTE_UN_ELEMENT))
    #Test d'une liste non répétée
    print("Résultat obtenu pour la liste ", LISTE_NON_REPETEE, ": ", a_repetitions(LISTE_NON_REPETEE))
    
    #Test de liste répétée
    print("Résultat attendu: True")
    #Test d'une liste répétée en fin de liste
    print("Résultat obtenu pour la liste ", LISTE_REPETEE_1, ": ", a_repetitions(LISTE_REPETEE_1))
    #Test d'une liste répétée en début de liste
    print("Résultat obtenu pour la liste ", LISTE_REPETEE_2, ": ", a_repetitions(LISTE_REPETEE_2))
    #Test d'une liste répétée en milieu de liste
    print("Résultat obtenu pour la liste ", LISTE_REPETEE_3, ": ", a_repetitions(LISTE_REPETEE_3))
    
#test_a_repetitions()
