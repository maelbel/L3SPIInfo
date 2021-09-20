# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:32:03 2021

@author: maelb
"""

def reprographie()-> str:
    '''Fonction pour calculer le prix du nombre de photocopie
    outputs:
        str: message contenant la facture'''
    
    #Variables
    #On demande à l'utilisiteur d'entrer le nombre de photocopie et on l'enregistre dans une variable
    nombre_copie = input("Veuillez saisir le nombre de photocopie: ")
    #On transforme cette variable en entier
    nombre_copie = int(nombre_copie)

    #Constantes
    COPIE_10 = 10
    COPIE_20 = 20
    COPIE_30 = 30
    
    COUT_COPIE_10 = 0.10
    COUT_COPIE_9 = 0.09
    COUT_COPIE_8 = 0.08
    
    #Si le nombre de copie est inférieur ou égale à 10
    if nombre_copie <= COPIE_10:
        #On facture la copie 0.10€
        facture = nombre_copie*COUT_COPIE_10
    else: #nb_copie > 10
        #if nb_copie >= 11:
        #Sinon on facture déjà les 10 premières copies 
        facture = COPIE_10*COUT_COPIE_10
        #Si le nombre de copie est inférieur ou égale à 30
        if nombre_copie <= COPIE_30:
            #On enlève les 10 premières copies déjà facturées 
            nombre_copie = nombre_copie - COPIE_10
            #On facture le nombre de copie qui reste 0.09€ la copie
            facture+=nombre_copie*COUT_COPIE_9
        else:
            #Sinon on facture déjà les 20 copies suivantes 
            facture += COPIE_20*COUT_COPIE_9
            #On enlève les 30 premières copies déjà facturées 
            nombre_copie = nombre_copie-COPIE_30
            #Et on facture le reste des copies 0.08€ la copie
            facture += nombre_copie*COUT_COPIE_8
    
    message = "Votre facture s'élève à "+str(facture)+"€"
    return message
    
#On lance la fonction
print(reprographie())