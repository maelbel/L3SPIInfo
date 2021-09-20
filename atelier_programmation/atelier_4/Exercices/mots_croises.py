# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:34:27 2021

@author: maelb
"""
import random
def mot_n_lettres(lst_mot: [str], nombre:int)-> [str]:
    """Fonction qui renvoie la liste des mots contenant exactement n lettres
    inputs:
        lst_mot: list Représente une liste mot
        n: int Représente un entier
    outputs:
        [str]: Retroune une liste de mot supérieur à n"""

    #Variables
    taille_l = len(lst_mot)
    lst = []

    #Pour tout les mots de la liste
    for i in range(taille_l):
        #On récupère le mot et sa taille
        mot = lst_mot[i]
        taille_mot = len(mot)
        #Si le mot fait la même taille que l'entier nombre
        if taille_mot == nombre:
            #On ajoute le mot dans liste lst
            lst.append(mot)

    return lst

#print(mot_n_lettres(["jouer","bonjour", "punir", "jour",
#"aurevoir", "revoir", "pouvoir", "cour", "abajour",
#"finir", "aimer"], 4))

def commence_par(mot:str, prefixe:str)-> bool:
    """Fonction qui renvoie la liste des mots contenant exactement n lettres
    inputs:
        mot: str Représente une chaine de caracteres
        prefixe: str Représente une chaine de caracteres
    outputs:
        boolean: True si l'argument mot commence par prefixe et False sinon"""
    #Variables
    taille_p = len(prefixe)
    valide = True
    compteur = 0

    #Tant que c'est valide et la taille du préfixe n'est pas dépassé
    while valide and compteur < taille_p:
        #Si la lettre l du mot n'est pas égale a la lettre l du préfixe
        if mot[compteur] != prefixe[compteur]:
            #Le mot ne commence pas par le préfixe et la boucle s'arrête
            valide = False
        else:
            compteur += 1

    return valide

#print(commence_par("inévitable", "inet"))

def finit_par(mot:str, suffixe:str)-> bool:
    """Fonction qui renvoie la liste des mots contenant exactement n lettres
    inputs:
        mot: str Représente une chaine de caracteres
        prefixe: str Représente une chaine de caracteres
    outputs:
        boolean: True si l'argument mot commence par prefixe et False sinon"""
    #Variables
    taille_m = len(mot)
    valide = True
    compteur = taille_m #Pour commencer à la fin du mot

    #Tant que c'est valide et la taille du suffixe n'est pas dépassé
    while valide and compteur < taille_m:
        #Si la lettre l du mot n'est pas égale a la lettre l du suffixe
        if mot[compteur] != suffixe[compteur]:
            #Le mot ne finit pas par le suffixe et la boucle s'arrête
            valide = False
        else:
            compteur -= 1

    return valide

#print(finit_par("inévitable", "beeeele"))

def finissent_par(lst_mot:[str], suffixe:str)-> [str]:
    """Fonction qui renvoie la liste des mots finissant par suffixe
    inputs:
        lst_mot: list Représente une liste mot
        préfixe: str Représente un mot
    outputs:
        [str]: Retourne une liste de mot finissant par suffixe"""

    #Variables
    taille_l = len(lst_mot)
    lst = []

    #Pour tous les mots de la liste
    for i in range(taille_l):
        #On récupère le mot
        mot = lst_mot[i]

        #Si le mot finit par le suffixe
        if finit_par(mot, suffixe):
            #On ajoute le mot à la liste lst
            lst.append(mot)

    return lst

#print(finissent_par(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
#"finir", "aimer"], "oir"))

def commencent_par(lst_mot:[str], prefixe:str)-> [str]:
    """Fonction qui renvoie la liste des mots commençant par préfixe
    inputs:
        lst_mot: list Représente une liste mot
        préfixe: str Représente un mot
    outputs:
        [str]: Retourne une liste de mot commençant par préfixe"""

    #Variables
    taille_l = len(lst_mot)

    lst = []

    #Pour tous les mots de la liste
    for i in range(taille_l):
        #On récupère le mot
        mot = lst_mot[i]

        #Si le mot commence par le préfixe
        if commence_par(mot, prefixe):
            #On ajoute le mot à la liste lst
            lst.append(mot)

    return lst

#print(commencent_par(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
#"finir", "aimer"], "jou"))

def liste_mots(lst_mot:[str], prefixe:str, suffixe:str, nombre:int)-> [str]:
    """Fonction
    inputs:
        lst_mot: [str] Représente une liste de mot
        prefixe: str Représente un préfixe
        suffixe: str Représente un suffixe
        nombre: int Représente un entier
    outputs:
        [str]: """

    #Variables
    #On récupère les mots de la liste lst_mot commençant par le préfixe
    commencent = commencent_par(lst_mot, prefixe)
    #On récupère les mots de la liste commencent finissant par le suffixe
    finissent = finissent_par(commencent, suffixe)
    #On récupère les mots de la liste finissent ayant le même nombre de lettre que l'entier nombre
    liste = mot_n_lettres(finissent, nombre)

    return liste

#print(liste_mots(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
#"finir", "aimer"], "a", "r", 5))

def dictionnaire(fichier:str)-> [str]:
    """Procédure qui affiche le contenu d'un fichier .txt
    inputs:
        fichier: str Représente le nom du fichier à ouvrir
    outputs:
    [str]: Représente une liste de tout les mots présent dans le fichier"""
    #Variables
    lst_mot = []
    #On ouvre le fichier avec un encodage utf-8
    with open(fichier, encoding="utf8") as file:
        #On lit et enregistre la première ligne
        line = file.readline()
        #Tant que le fichier n'est pas terminé
        while line != "":
            #On ajoute le mot à la liste
            lst_mot.append(line)
            #On passe à la ligne suivante
            line = file.readline()

    return lst_mot

print(dictionnaire("littre.txt"))

def test_exercice1():
    """
        procédure de test
    """
    #variable
    lst_mot = ["jouer","bonjour", "punir", "jour", "aurevoir", "revoir","pouvoir",
               "cour", "abajour","finir", "aimer"]
    i_rand = random.randint(0, len(lst_mot)-1)
    mot = lst_mot[i_rand]
    print(mot)
    prefixe = str(input("Veuillez rentrer un prefixe :"))
    suffixe = str(input("Veuillez rentrer un suffixe :"))
    num = int(input("Veuillez entrer la taille du mot :"))
    #tests
    print("Résultat attendu : True")
    print(commence_par(mot, prefixe))
    print("Résultat attendu : True")
    print(finit_par(mot, suffixe))

    print(commencent_par(lst_mot, prefixe))
    print(finissent_par(lst_mot, suffixe))
    print(mot_n_lettres(lst_mot, num))
    print(liste_mots(lst_mot, prefixe, suffixe, num))
#test_exercice1()
