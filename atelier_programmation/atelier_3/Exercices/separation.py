# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 17:59:32 2021

@author: maelb
"""
def separer(lst:list)-> list:
    """Fonction qui retourne une liste classée par chiffre négatif, égale à 0 et supérieur à 0.
    inputs:
        l: list Représente une liste non triée
    outputs:
        list: Retourne une liste classée dans l'ordre suivant: négatif, zéro, positif"""
    #Variables
    taille_l = len(lst)
    lsep = []
    #Pour tous les élément i de la liste l
    for i in range(taille_l):
        #On enregistre la taille actuel de la liste LSEP
        taille_lsep = len(lsep)
        #Si l'élément de la liste est inférieur à 0
        if lst[i] < 0:
            #On insert au début de la liste lsep l'élément i de la liste l
            lsep.insert(0, lst[i])
        #Sinon si l'élément de la liste est inférieur à 0
        elif lst[i] > 0:
            #On insert dans la liste lsep, à sa fin entière, l'élément i de la liste l
            lsep.insert(taille_lsep, lst[i])
        else:
            #Sinon (égale à 0)
            #Si la taille du tableau lsep est pair
            if taille_lsep%2 == 0:
                #On insert dans la liste lsep, à sa moitié, l'élément i de la liste l
                lsep.insert(int(taille_lsep/2), lst[i])
            else:
                #Sinon (impair)
                #On insert dans la liste lsep, à sa moitié entière, l'élément i de la liste l
                lsep.insert(int(taille_lsep//2), lst[i])
    return lsep
print(separer([1,-2,0,-2,-3,6,5,7,5,0,0,0,5,8,9,-5]))
