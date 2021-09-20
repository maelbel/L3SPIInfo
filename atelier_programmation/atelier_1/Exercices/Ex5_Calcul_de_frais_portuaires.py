# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:32:03 2021

@author: maelb
"""

def frais_portuaire()-> str:
    """Procédure pour calculer les frais mensuel d'une place d'un voilier au port"""
    
    #Variables
    #On demande à l'utilisateur de rentrer le nom de son voilier et on l'enregistre dans une variable
    nom = input("Saisir le nom de votre voilier: ")
    #On demande à l'utilisateur de rentrer la longueur de son voilier et on l'enregistre dans une variable
    longueur = int(input("Saisir la longueur de votre voilier: "))
    #On demande à l'utilisateur de rentrer la catégorie de son voilier et on l'enregistre dans une variable
    categorie = int(input("Saisir la catégorie de votre voilier: "))
    
    taxe_annuelle = 0

    #Constantes
    LONGEUR_1 = 5
    LONGEUR_2 = 10
    LONGEUR_3 = 12
    
    COUT_MENSUEL_1 = 100
    COUT_MENSUEL_2 = 200
    COUT_MENSUEL_3 = 400
    COUT_MENSUEL_4 = 600
    
    TAXE_SPECIAL_ANNUELLE_1 = 100
    TAXE_SPECIAL_ANNUELLE_2 = 150
    TAXE_SPECIAL_ANNUELLE_3 = 250
    
    CATEGORIE_1 = 1
    CATEGORIE_2 = 2
    
    #Si la longueur du voilier est inférieur à 5 mètres
    if longueur < LONGEUR_1:
        #On enregistre le cout mensuel à 100€
        cout_mensuel = COUT_MENSUEL_1
    #Sinon si la longueur du voilier est inférieur ou égale à 10 mètres
    elif longueur <= LONGEUR_2:
        #On enregistre le cout mensuel à 200€
        cout_mensuel = COUT_MENSUEL_2
    else:
        #Sinon
        #Si la longueur du voilier est inférieur ou égale à 12 mètres
        if longueur <= LONGEUR_3:
            #On enregistre le cout mensuel à 400€
            cout_mensuel = COUT_MENSUEL_3
        else:
            #Sinon on enregistre le cout mensuel à 600€
            cout_mensuel = COUT_MENSUEL_4
    
    print("Le coût mensuel est de "+str(cout_mensuel)+"€")
    
    #Si le bateau fait partie de la catégorie 1
    if categorie == CATEGORIE_1:
        #On enregistre la taxe speciale annuelle à 100€
        taxe_speciale_annuelle = TAXE_SPECIAL_ANNUELLE_1
    #Sinon si le bateau fait partie de la catégorie 2
    elif categorie == CATEGORIE_2:
        #On enregistre la taxe speciale annuelle à 150€
        taxe_speciale_annuelle = TAXE_SPECIAL_ANNUELLE_2
    #Sinon le bateau fait partie de la catégorie 3
    else:
        #On enregistre la taxe speciale annuelle à 250€
        taxe_speciale_annuelle = TAXE_SPECIAL_ANNUELLE_3
        
    print("La taxe speciale annuelle est de "+str(taxe_speciale_annuelle)+"€")
    
    #On calcule la taxe annuelle et on l'affiche avec la concaténation
    taxe_annuelle = cout_mensuel*12 + taxe_speciale_annuelle
    print("Le coût annuel d’une place au port pour le voilier "+str(nom)+" est de "+str(taxe_annuelle)+" euros.")
    

frais_portuaire()