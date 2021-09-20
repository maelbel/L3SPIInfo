# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:32:03 2021

@author: maelb
"""

def concessionnaire_automobile()-> str:
    """Fonction pour calculer le cout mensuel d'une voiture
    outputs:
        str: message contenant le cout mensuel d'une voiture"""
    
    #Variables
    #On demande et enregistre le kilométrage par an de l'utilisateur dans une variable
    kilometre_par_an = int(input("Veuillez saisir le nombre de kilomètre que vous parcourez par an: "))
    #On demande et enregistre le type de carburant de la voiture de l'utilisateur dans une variable
    type_carburant = str(input("Veuillez saisir le type de carburant utilisé (D pour diesel, E pour essence): "))
    #On demande et enregistre la cylindrée de la voiture de l'utilisateur dans une variable
    taille_cylindree = int(input("Veuillez saisir la cylindré de la voiture: "))
    #On demande et enregistre le prix du carburant de l'utilisateur dans une variable
    prix_carburant = float(input("Veuillez saisir le prix du carburant: "))
    
    #Constantes
    CARBURANT_E = 'E'
    TAILLE_CYLINDREE_2000 = 2000
    DIX_LITRE_CENT = 0.10
    HUIT_LITRE_CENT = 0.08
    SURCOUT_50 = 1+50/100
    SURCOUT_70 = 1+70/100
    
    #Si le type de carburant est de l'essence
    if type_carburant == CARBURANT_E:
        #Et si la taille de la cylindrée est supérieur à 2000cm3
        if taille_cylindree > TAILLE_CYLINDREE_2000:
            #On calcule le carburant utilisé en un an par une essence avec une consommation de 8 litres aux 100 km
            carburant_utilise = kilometre_par_an*DIX_LITRE_CENT
            #On calcule le cout du carburant en un an
            cout_carburant = carburant_utilise*prix_carburant
        else:
            #Sinon on calcule le carburant utilisé en un an par une essence avec une consommation de 8 litres aux 100 km
            carburant_utilise = kilometre_par_an*HUIT_LITRE_CENT
        surcout = SURCOUT_50
    else:
        #Sinon on calcule le carburant utilisé en un an par une diesel avec une consommation de 8 litres aux 100 km
        carburant_utilise = kilometre_par_an*HUIT_LITRE_CENT
        surcout = SURCOUT_70
        
    cout_carburant = carburant_utilise*prix_carburant
    cout_carburant = cout_carburant + cout_carburant*surcout
    #On calcule le cout mensuel et on l'affiche
    cout_mensuel = cout_carburant/12
    
    print("Le cout mensuel est de "+str(cout_mensuel)+"€")
    return cout_mensuel

concessionnaire_automobile()