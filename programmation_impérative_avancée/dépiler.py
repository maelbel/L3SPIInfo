# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:22:18 2021

@author: maelb
"""

import numpy as np

Tab = np.random.randint(1,100,10)
print(Tab)

def dépiler():
    for i in range(1, len(Tab-1)):
        ind = 0
        F = i-1
        while (ind*2+1 <= F):
            PP = ind*2+1
            if((ind+1)*2 <= F and Tab[PP]>Tab[(ind+1)*2]):
                PP = (ind+1)*2
            Tab[ind] = Tab[PP]
            ind = PP
            
dépiler()
print(Tab)