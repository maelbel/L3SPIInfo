# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:43:26 2021

@author: maelb
"""

TA = [5, 4, 3, 2, 1]
TB = []
TC = []

def hanoi(N, TA, TB, TC, Nom1, Nom2, Nom3):
    if(N == 1):
        print("Je déplace ", TA[-1], " de ", Nom1, " => ", Nom2)
        TB.append(TA[-1])
        del TA[-1]
    else:
        hanoi(N-1, TA, TC, TB, Nom1, Nom3, Nom2)
        hanoi(1, TA, TB, TC, Nom1, Nom2, Nom3)
        hanoi(N-1, TC, TB, TA, Nom3, Nom2, Nom1)

hanoi(5, TA, TB, TC, "TA", "TB", "TC")
print("TA: ", TA)
print("TB: ",TB)
print("TC: ",TC)