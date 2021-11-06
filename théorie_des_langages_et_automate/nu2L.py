# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:32:23 2021

@author: maelb
"""
def nu2str(u:str)-> int:
    """Fonction"""
    
    #Variables
    S = 0
    n = len(u)
    L = range(n)
    
    for i in L:
        S = 2 * S + int(u[i])
    
    return S

print(nu2str("1010"))