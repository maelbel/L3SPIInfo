# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:59:03 2021

@author: maelb
"""
def gloutonStr(m:int, base:int)-> str:
    """Fonction qui transforme base 10 en base 3"""

    #variables
    p = 1
    u = ""

    while base*p <= m:
        p = base*p

    while p>0:
        u = u + str(m//p)
        m = m%p
        p = p//base

    return u

print(gloutonStr(1789,2))