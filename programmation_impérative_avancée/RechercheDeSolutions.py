# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:37:19 2021

@author: maelb
"""
V = [0, 0]
R = [0, 1]
gamma = 1
iterations = 100000
for i in range(iterations):
    V[0] = R[0]+gamma*V[1]
    V[1] = R[1]+gamma*V[0]
    if i%10000==0:
        print(V)