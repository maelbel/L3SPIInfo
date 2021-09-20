# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:08:33 2021

@author: maelb
"""
from datetime import date
from annee_bissextile import est_bissextile

def date_est_valide(jour:int, mois:int, annee:int)-> bool:
    """Fonction qui détermine si la date est valide
    inputs:
        jour: int représente le jour à tester
        mois: int représente le mois à tester
        annee: int représente l'année à tester
    outputs:
        boolean: True si l'année est bissextile, False si elle ne l'est pas"""
    
    #Variables
    valide = True
    bissextile = est_bissextile(annee)
    
    #CONSTANTES
    DAY_OF_MONTH = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #Si l'annee est bissextile
    if bissextile:
        #On change le jour max pour le deuxieme mois
        DAY_OF_MONTH[2] = 29

    if jour<1 or mois<1 or mois>12:
        valide = False
        
    return valide and jour<DAY_OF_MONTH[mois]

def saisie_date_naissance()-> date:
    """Fonction pour saisir la date
    outputs:
        date: renvoie la date saisi sous forme AAAA/MM/JJ
        error: str Affiche une erreur"""
        
    #Variables
    jour = int(input("Veuillez saisir votre jour de naissance (JJ): "))
    mois = int(input("Veuillez saisir votre mois de naissance (MM): "))
    annee = int(input("Veuillez saisir votre jour de naissance (AAAA): "))
    
    #Si la date saisie est valide
    if date_est_valide(jour, mois, annee):
        #On retourne la date sous forme AAAA/MM/JJ
        date_naissance = date(annee,mois,jour)
    else:
        #Sinon on affiche un message d'erreur
        print("Erreur... Date invalide.")

    return date_naissance

def age(date_naissance:date)-> int:
    """Fonction pour donner l'age de l'utilisateur
    inputs:
        date_naissance: date Représente la date de naissance sous forme AAAA/MM/JJ
    outputs:
        age_u: int Renvoie l'âge"""
    
    #CONSTANTES
    AUJOURDHUI = date.today()
    JOUR = AUJOURDHUI.day
    MOIS = AUJOURDHUI.month
    ANNEE = AUJOURDHUI.year
    
    JOUR_NAISSANCE = date_naissance.day
    MOIS_NAISSANCE = date_naissance.month
    ANNEE_NAISSANCE = date_naissance.year
    
    age_u = ANNEE - ANNEE_NAISSANCE
    
    if MOIS_NAISSANCE > MOIS or (MOIS_NAISSANCE == MOIS and JOUR_NAISSANCE < JOUR):
        age_u -= 1
    
    return age_u

def est_majeur(date_naissance:int)-> bool:
    """Fonction pour déterminer si l'utilisateur est majeur ou mineur
    inputs:
        date_naissance: int Représente l'âge de l'utilisateur
    outputs:
        boolean: True si l'utilisateur est majeur, False s'il ne l'est pas"""
    #CONTANTES
    MAJEUR = 18
    
    return date_naissance>MAJEUR

def test_acces()-> str:
    """Fonction pour afficher un message d'accueil selon l'âge
    outputs:
        string: Affiche si l'utilisateur à accès ou non"""
    
    #Variables
    date_naissance = saisie_date_naissance()
    
    #Si l'utilisateur est majeur
    if est_majeur(age(date_naissance)):
        #On crée un message d'accès autorisé
        message = "Bonjour, vous avez "+str(age(date_naissance))+" ans, Accès autorisé"
    else: 
        #Sinon on crée un message d'accès refusé
        message = "Désolé, vous avez "+str(age(date_naissance))+" ans, Accès interdit"

    return print(message)

def test()-> None:
    """Procédure de test
    outputs: None"""
    test_acces()

test()
