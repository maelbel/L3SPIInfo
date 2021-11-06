# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:10:52 2021

@author: maelb
"""

import numpy as np
import sys
import copy

def lireReseau()-> list:
    """Fonction qui retourne un reseau et ces sommets"""
    Reseau = np.loadtxt("reseau.txt", dtype = int)
    Sommets = []
    
    for i in range(len(Reseau)):
        Sommets.append("S"+str(i))
        
    return Reseau, Sommets
    
Reseau, Sommets = lireReseau()

PccCh = []
PccKm = sys.maxsize
Ch = []
Km = 0

def Rechercher(D, A):
    """Fonction pour rechercher le plus court chemin du reseau"""
    global PccCh, PccKm, Ch, Km
    if D == A:
        PccCh = copy.deepcopy(Ch)
        PccKm = Km
        return
    indD = Sommets.index(D)
    
    for V in [S for S in Sommets if S not in Ch]:
        indV = Sommets.index(V)
        if Reseau[indD, indV] > 0 and PccKm > Km + Reseau[indD, indV]:
            Ch.append(V)
            Km += Reseau[indD, indV]
            Rechercher(V, A)
            del Ch[-1]
            Km -= Reseau[indD, indV]
            
D = "S0"
A = "S5"
Ch.append(D)
Rechercher(D, A)
print(PccCh)
print(PccKm)