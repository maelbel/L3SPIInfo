# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:14:28 2021

@author: maelb
"""
def convert3(m:int)-> str:
    """Fonction qui transforme base 10 en base 2"""
    
    #Variable
    u = ""
    
    while m > 0:
        u = str(m%3) + u
        m = m//3
        
    return u

print(convert3(9))