# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 09:21:26 2021

@author: maelb
"""

import numpy as np

Taille = 8
Trouve = False
TabOfReines = [0]*Taille

def accepter(e, numReine):
    """"""
    if e in TabOfReines:

def placerReines(numReine):
    """"""
    if numReine==Taille :
        Trouve = True; return
        
    for e in range(Taille):
        if accepter(e):
            TabOfReines[numReine] = e
            placerReines(numReine + 1)
            if Trouve: return
            TabOfReines[numReine] = 0