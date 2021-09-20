# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 10:54:00 2021

@author: maelb
"""
import random
def place_lettres(char:str, mot:str)-> [str]:
    """Fonction qui retourne une liste d'indice
    inputs:
        char: str Représente un caractère
        mot: str Représent un mot
    outputs:
        [str]: une liste d'indice représentant la place du caractère dans le mot"""
    #Variables
    taille_m = len(mot)
    liste = []
    for i in range(taille_m):
        if char == mot[i]:
            liste.append(i)
    return liste
#Þprint(place_lettres("m", "maman"))

def output_str(mot:str, lpos:[int])-> str:
    """Fonction qui retourne une chaine de caractère
    inputs:
        mot: str Représente une chaine de caractère, soit un mot
        lpos: [int] Représente une liste d'entier'
    outputs:
        str: """

    #Variables
    taille_m = len(mot)
    message = ""

    #Pour toutes les positions de lettres du mot
    for position_l in range(taille_m):
        #Si la position est dans la liste lpos
        if position_l in lpos:
            #On ajoute la lettre au message
            message += mot[position_l]
        else:
            #Sinon on ajoute un " _ "
            message += " _ "

    return message

#print(output_str("Fromage", [0,1,2,3,4,5,6,7]))

def build_list(file_name:str)-> [str]:
    """Fonction qui retourne la liste de toutes les capitales du monde
    inputs:
        file_name: str Représente le nom du fichier à utiliser
    outputs:
        [str]: Retourne une liste de capitales"""

    #Variables
    content = []

    #On ouvre et lit le fichier
    with open(file_name, encoding = 'utf-8') as file:
        #On enregistre tout son contenu
        content = file.readlines()
        #On coupe content au niveau des tabulations
        content = content[0].split("\t")

        taille_liste = len(content)
        #Pour toutes les capitales
        for capitale in range(taille_liste):
            #On met tout en lettre minuscule
            content[capitale] = content[capitale].lower()

    return content

def build_dict(lst:list)-> dict:
    """Fonction qui retourne un dictionnaire à partir d'une liste de mot
    inputs:
        lst: [str] Représente une liste de mot
    ouputs:
        dict: Retourne un dictionnaire"""

    #Variables
    dictionnaire = {}

    #Pour tous les mots de la liste
    for mot in lst:
        taille_m = len(mot)
        #Si la taille du mot est dans la liste
        if taille_m in dictionnaire:
            #On ajoute le mot à la clé taille_m
            dictionnaire[taille_m].append(mot)
        else:
            #On ajoute le mot au dictionnaire à la clé taille_m
            dictionnaire[taille_m] = [mot]

    return dictionnaire

def select_word(sorted_words:dict, word_len:int)-> str:
    """Fonction qui retourne un mot choisi au hasard dans la liste des mots de taille word_len
    inputs:
        sorted_word: dict Représente un dictionnaire
        word_len: int Représente la taille des mots à selectionner
    outputs:
        str: Retourne le mot à trouver"""

    #Variables
    lst_mot = sorted_words.get(random.randint(0, word_len))

    #Tant que la liste de mot est vide
    while lst_mot is None:
        lst_mot = sorted_words.get(random.randint(0, word_len))

    taille_l = len(lst_mot) #Taille de la liste
    i_rand = random.randint(0, taille_l-1) #Nombre random entre 0 et taille_l
    mot = lst_mot[i_rand] #On récupère un mot random

    return mot

#print(select_word({5:['paris'],6:['madrid','berlin'],7:['londres','newyork']}, 7))

def run_game()-> None:
    """Procédure qui lance le jeu du pendu
    outputs: None"""

    #Variables
    lst = build_list("capitales.txt")
    taille_l = len(lst)
    #Recherche du mot le plus long dans la liste
    taille_m = 0
    taille_m_max = 0
    for mot in range(taille_l):
        taille_m = len(lst[mot])
        if taille_m > taille_m_max:
            taille_m_max = taille_m

    taille_mot = 0
    #Saisie de la difficulté
    print("Difficulté 1: Mot inférieur ou égale à 6 lettres")
    print("Difficulté 2: Mot à 7 ou 8 lettres")
    print("Difficulté 3: Mot supérieur ou égale à 9 lettres")

    taille_mot = int(input("Veuillez saisir le niveau de difficulté (1-2-3): "))

    if taille_mot == 1: #Difficulté 1
        taille_mot = 6
    elif taille_mot == 2: #Difficulté 2
        taille_mot = random.randint(7,8)
    else:                   #Difficulté 3
        taille_mot = random.randint(9,taille_m_max)

    mot = select_word(build_dict(lst), taille_mot)
    print(mot)
    #Initialisation des erreurs
    nb_erreurs = 0
    AFFICHAGE_ERREUR = ["|______", r"|/ \ ", "| T ", "| O ", "|---] "]
    nb_erreurs_max = len(AFFICHAGE_ERREUR)

    #Pour une meilleure lecture dans la console
    print("\n\n")

    #On affiche le nombre de lettre à trouver
    affichage = output_str(mot, [])
    print(affichage)

    #Pour tester si il n'y a pas la lettre dans le mot
    test_vide = []
    place_lettre = []

    lettre_utilisees = "" #Affiche toutes les lettres utilisées
    trouve = False #Pour fermer la boucle while si on trouve le mot
    coups = 0

    #Tant que le mot n'est pas trouvé et que le nombre de coups est inférieur à la limite
    while not trouve and nb_erreurs < nb_erreurs_max:
        #On demande de saisir un caractère
        lettre = input("Veuillez entrer une lettre: ")
        print("\n") #Pour une meilleure lecture dans la console
        #On enregistre les emplacements de cette lettre dans le mot
        test_vide = place_lettres(lettre, mot) #Test si c'est vide
        place_lettre += place_lettres(lettre, mot) #Accumulent la place des lettres saisies

        #Si la liste des places des lettres est vide
        if test_vide == []:
            #On ajoute une erreurs
            nb_erreurs += 1

        #Et pour toutes les erreurs effectués
        #On parcours le tableau d'affichage des erreurs en décroissant
        for i in range(nb_erreurs_max, 0, -1):
            #Si l'erreur est supérieur ou égale à i
            if nb_erreurs >= i:
                #On affiche les parties d'erreurs correspondantes
                print(AFFICHAGE_ERREUR[i-1])
        print("\n")#Pour une meilleure lecture dans la console

        #Si le mot est sortant de la fonction output_str est égale au mot à trouver
        if output_str(mot, place_lettre) == mot:
            #On a trouvé le mot
            trouve = True

        #On affiche les lettres trouvées
        print(output_str(mot, place_lettre), "\n")

        #On affiche le nombre de coup restant
        cout_restant = nb_erreurs_max - nb_erreurs
        print("Il vous reste", cout_restant, "erreur(s) restante(s) \n")

        #On affiche les lettres utilisées
        lettre_utilisees += lettre + " - "
        print("Vous avez déjà utilisé les lettres suivantes: ", lettre_utilisees, "\n")

        coups += 1

    #Si le mot est trouvé
    if trouve:
        print("Bravo ! Vous avez trouvé le mot", mot, "en", coups,"coups")
    else: #Sinon
        print("Dommage... Vous n'avez pas trouvé le mot", mot, "\n Retentez votre chance !")

run_game()
