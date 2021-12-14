# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:15:09 2021

@author: maelb
"""
def convertK(m:int, base:int)-> str:
    """Fonction qui transforme base 10 en base 2"""
    
    #Variable
    u = ""
    
    while m > 0:
        u = str(m%base) + u
        m = m//base
        
    return u

print(convertK(11, 3))