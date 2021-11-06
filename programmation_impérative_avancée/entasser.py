# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:55:30 2021

@author: maelb
"""

import numpy as np

Tab = np.random.randint(1,100,10)
print(Tab)

def entasser():
    for i in range(1, len(Tab)):
        ind = i
        while (ind > 0) and (Tab[ind] < Tab[(ind-1)//2]):
            Tab[ind], Tab[(ind-1)//2] = Tab[(ind-1)//2], Tab[ind]
            ind = (ind-1)//2
            
entasser()
print(Tab)