# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:57:19 2021

@author: maelb
"""
def gloutonK(m:int, base:int)-> str:
    """Fonction qui transforme base 10 en base 3"""

    #variables
    p=1
    u=[]

    while base*p <= m:
        p=base*p

    while p>0:
        u=u+[m//p]
        m=m%p
        p=p//base

    return u

print(gloutonK(1789,3))