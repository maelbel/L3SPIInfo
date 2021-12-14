# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:17:23 2021

@author: maelb
"""

def gloutonFibo(m:int)-> str:
    """Fonction qui transforme base 10 en base Fibonacci"""

    #variables
    u = ""

    F0 = 1
    F1 = 2
    
    while F1 <= m:
        F1 = F0 + F1
        F0 = F1 - F0

    while F1 > 1:
        u = u + str(m//F0)
        m = m%F0
        F0 = F1 - F0
        F1 = F1 - F0

    return u

print(gloutonFibo(7))