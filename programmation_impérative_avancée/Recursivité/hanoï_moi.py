# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:10:52 2021

@author: maelb
"""

import numpy as np

def lireReseau():
    Reseau = np.loadtxt("reseau.txt", dtype = int, )
    
def Pcc(D, A, L, ch, Dp, Pcch, PccDp):
    """Fonction pour trouver tous les chemins d'un lymbyrinthe de façon récursive"""
    
    if D == A:
        if PccDt > Dt:
            ch = Pcch
            Dt = PccDt
    
    for v in D:
        ch += v
        Dt += R[D, v]
        
        if Dt > PccDt:
            Pcc(v, A, L-v, ch, Dp, Pcch, PccDp)
            if A = S:
                
            else:
                ch -= v
                Dt -= R[D, v]

L = 
PccDt = 99999999
