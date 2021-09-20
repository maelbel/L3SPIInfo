# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:56:53 2021

@author: maelb
"""
import re

def full_name(str_arg:str)-> str:
    """Fonction qui retourne le nom de famille en majuscule et le prénom
    inputs:
        str_arg: str Représente le nom et et prénom
    outputs:
        str: Retourne le nom en upper et le prénom en capitalize"""
    
    #Variables
    str_arg = str_arg.upper()
    lst_str = str_arg.split(" ")
    taille_l = len(lst_str)
    
    #On récupère le prénom et sa taille
    prenom = lst_str[taille_l-1]
    
    #Si le trait d'union est présent dans le prénom
    if "-" in prenom:
        #C'est une prénom composé
        #On coupe le prénom en deux à partir du "-" ainsi que sa taille
        prenom_lst = prenom.split("-")
        taille_prenom_liste = len(prenom_lst)
        
        #Pour tous les prénoms (Ex de prenom_lst: ["JEAN", "BAPTISTE"])
        for j in range(taille_prenom_liste):
            #On les capitalize
            prenom_lst[j] = prenom_lst[j].capitalize()
        
        #Et pour finir on les joints avec un "-"
        prenom = "-".join(prenom_lst)
        #Et on change les modifications faites dans la liste lst_str
        lst_str[taille_l-1] = prenom
    else:
        #Sinon on capitalize le prenom
        lst_str[taille_l-1] = lst_str[taille_l-1].capitalize()
        
    #Et pour terminer on join le nom et le prenom
    str_arg = " ".join(lst_str)
    
    return str_arg

def test_full_name()-> None:
    """Procédure de test
    outputs: None"""
    print(full_name("belliard mael"))
    print(full_name("Ottavi-Nedelec Nicolas"))
    print(full_name("orsoni pierre-jean"))
    print(full_name("de miranda lopes alexandre"))

#test_full_name()

def is_mail(str_arg:str)-> (int, int):
    """Fonction qui retourne le nom de famille en majuscule et le prénom
    inputs:
        str_arg: str Représente une adresse mail
    outputs:
        (int, int): Représente un code d'erreur ou de validité"""
        
    #Variables
    code = (1, 0)
    local = ""
    domaine = ""
    local_match = ""
    domaine_match = ""
    
    #Si l'arobase est présent
    if "@" in str_arg:
        #On split le mail
        lst_str = str_arg.split("@")
        #On garde la partie local et domaine dans des variables différentes pour les tester après
        local = lst_str[0]
        domaine = lst_str[1]
        #On enregistre le match necessaire pour la validité de la partie locale
                                 #[1 ou plusieurs](0, 1 ou plusieurs)(\. : interprète pas le point)
        local_match = re.match(r"[A-Za-z0-9.-]+(\.[A-Za-z0-9._-])*", local)
        #Si local est dans le mail et que le match est none
        if local in str_arg and local_match is None:
            #Le code d'erreur est (0, 1)
            code = (0, 1)
        
        #Si le point est dans la partie domaine
        if "." in domaine:            
            #On enregistre le match necessaire pour la validité de la partie domaine
            domaine_match = re.match(r"[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", domaine)
            
            #Si nom_service est dans le mail et que le match est none
            if domaine in str_arg and domaine_match is None:
                #Le code d'erreur est (0, 3)
                code = (0, 3)
        else:
            #Sinon le code d'erreur est (0, 4)
            code = (0, 4)
    else:
        #Sinon le code d'erreur est (0, 2)
        code = (0, 2)

    return code

def test_is_mail():
    """Procédure de test
    outputs:
        None"""
        
    code_mail_1 = "mael.belliard@laposte.net"
    code_mail_2 = "%%µ*$@laposte.net"
    code_mail_3 = "mael.belliard.laposte.net"
    code_mail_4 = "mael.belliard@%$ù**$.net"
    code_mail_5 = "mael.belliard@lapostenet"
    code_mail_6 = "mael.belliard@laposte.£%µ"
    
    print("Résultat attendu : (1, 0)")
    print("Le mail", code_mail_1, "est un mail", is_mail(code_mail_1), "\n\n")
    
    print("Résultat attendu : (0, 1)")
    print("Le mail", code_mail_2, "est un mail", is_mail(code_mail_2), "\n\n")
    
    print("Résultat attendu : (0, 2)")
    print("Le mail", code_mail_3, "est un mail", is_mail(code_mail_3), "\n\n")
    
    print("Résultat attendu : (0, 3)")
    print("Le mail", code_mail_4, "est un mail", is_mail(code_mail_4), "\n\n")
    
    print("Résultat attendu : (0, 4)")
    print("Le mail", code_mail_5, "est un mail", is_mail(code_mail_5), "\n\n")
    
    print("Résultat attendu : (0, 5)")
    print("Le mail", code_mail_6, "est un mail", is_mail(code_mail_6), "\n\n")
    
#test_is_mail()

def text_is_mail() -> bool:
    """Fonction de test de la fonction is_mail()
    Returns:
        bool: True si tous les tests sont valides, False sinon
    """
    EMAIL_TO_TEST = {
        "bisgambiglia_paul@univ-corse.fr":(1,0),
        "bisgambiglia_paul@univ-corse.fr  ":(1,0),
        "bisgambiglia_paul@academie.univ-corse.fr":(1,0),
        "bisgambiglia_paul@academie.univ.corse.fr":(1,0),
        "@univ-corse.fr":(0,1),
        "bisgambiglia_paulOuniv-corse.fr":(0,2),
        "bisgambiglia_paul@.fr":(0,3),
        "bisgambiglia_paul@univ corse.fr":(0,3),
        "bisgambiglia_paul@univ-corsePOINTfr":(0,4)
    }
    nbr_test_valide = 0
    for value_to_test in EMAIL_TO_TEST.items():
        str_affichage = "Test : \"{}\", resultat attendu : {}, resultat obtenu : {}, reussit : ".format(value_to_test[0],value_to_test[1],str(is_mail(value_to_test[0])))
        if value_to_test[1] == is_mail(value_to_test[0]):
            str_affichage += "Oui"
            nbr_test_valide += 1
        else:
            str_affichage += "Non"
        print(str_affichage)

    if nbr_test_valide == len(EMAIL_TO_TEST):
        res = True
    else:
        res = False
    return res

print (
    text_is_mail()
)
