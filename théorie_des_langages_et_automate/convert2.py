# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:10:30 2021

@author: maelb
"""
def convert2(m:int):
    """Fonction qui transforme base 10 en base 2"""
    
    #Variable
    u = ""
    
    while m > 0:
        u = str(m%2) + u
        m = m//2
        
    return u

print(convert2(11))