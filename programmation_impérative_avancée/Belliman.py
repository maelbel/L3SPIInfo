# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:16:50 2021

@author: maelb
"""
import numpy as np
gamma = 0.95
iterations = 100
P = [[["Sud", 3, 0.5, 4, 0.5], ["Est", 1, 0.7, 4, 0.3]],
    [["Ouest", 0, 0.7, 3, 0.3], ["Sud", 3, 0.25, 4, 0.5, 5, 0.25], ["Est", 2, 0.7, 5, 0.3]],
    [["Ouest", 1, 0.7, 4, 0.3], ["Sud", 4, 0.5, 5, 0.5]],
    [["Nord", 0, 0.5, 1, 0.5], ["Sud", 6, 0.5, 7, 0.5], ["Est", 1, 0.25, 4, 0.5, 7, 0.25]],
    [["Nord", 0, 0.25, 1, 0.5, 2, 0.25], ["Sud", 6, 0.25, 7, 0.5, 8, 0.25], ["Ouest", 0, 0.25, 3, 0.5, 6, 0.25],  ["Est", 2, 0.25, 5, 0.5, 8, 0.25]],
    [["Ouest", 1, 0.25, 4, 0.5, 7, 0.25], ["Nord", 1, 0.5, 2, 0.5], ["Sud", 7, 0.5, 8, 0.5]],
    [["Ouest", 1, 0.70, 4, 0.3], ["Sud", 4, 0.5, 5, 0.5]],
    [["Nord", 3, 0.5, 4, 0.5], ["Est", 4, 0.3, 7, 0.7]],
    [["Ouest", 3, 0.3, 6, 0.7], ["Nord", 3, 0.25, 4, 0.5, 5, 0.25], ["Est", 5, 0.3, 8, 0.7]],
    [["Nord", 4, 0.5, 5, 0.5], ["Ouest", 4, 0.3, 7, 0.7]]
    ]

R = [[["Sud", 3, 0, 4, 0], ["Est", 1, 0, 4, 0]],
    [["Ouest", 0, 0, 3, 0], ["Sud", 3, 0, 4, 0, 5, 0], ["Est", 2, 0, 5, 0]],
    [["Ouest", 1, 0, 4, 0], ["Sud", 4, 0, 5, 0]],
    [["Nord", 0, 0, 1, 0], ["Sud", 6, 0, 7, 0], ["Est", 1, 0, 4, 0, 7, 0]],
    [["Nord", 0, 0, 1, 0, 2, 0], ["Sud", 6, 0, 7, 0, 8, 0], ["Ouest", 0, 0, 3, 0, 6, 0], ["Est", 2, 0, 5, 0, 8, 0]],
    [["Ouest", 1, 0, 4, 0, 7, 0], ["Nord", 1, 0, 2, 0], ["Sud", 7, 0, 8, 0]],
    [["Ouest", 1, 0, 4, 0.3], ["Sud", 4, 0, 5, 0]],
    [["Nord", 3, 0, 4, 0], ["Est", 4, 0, 7, 0]],
    [["Ouest", 3, 0, 6, 0], ["Nord", 3, 0, 4, 0, 5, 0], ["Est", 5, 0, 8, 0]],
    [["Nord", 4, 0, 5, 0], ["Ouest", 4, 0, 7, 0]]
    ]

Q = []
for s in range(len(P)):
    Q.append([0]*len(P[s]))

print(Q)

for i in range(iterations):
    for s in range(len(P)):
        for a in range(len(P[s])):
            somme = 0
            for ind in range(1, len(P[s][a]), 2):
                s_next = P[s][a][ind]
                somme += P[s][a][ind+1]*(R[s][a][ind+1]+gamma*np.max(Q[s_next]))
            Q[s][a] = somme
                
for s in range(len(P)):
    for a in range(len(P[s])):
        txt = f"Q[etat={s}, action={P[s][a][0]} = {Q[s][a]:.2f}"
        if a == np.argmax(Q[s]):
            txt = txt + " <= "
        print(txt)