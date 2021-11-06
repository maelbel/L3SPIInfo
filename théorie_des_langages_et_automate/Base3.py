# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:44:53 2021

@author: maelb
"""

def glouton3(m:int)-> str:
    """Fonction qui transforme base 10 en base 3"""

    #variables
    p=1
    u=[]

    while 3*p <= m:
        p=3*p

    while p>0:
        u=u+[m//p]
        m=m%p
        p=p//3

    return u

print(glouton3(1789))