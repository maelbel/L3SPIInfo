#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:01:41 2020

@author: bisgambiglia_p
"""

import numpy as np

Mat = np.loadtxt("Suddoku.txt")
print(Mat)    

def readLine(Mat, i) :
    return [x for x in Mat[i,0:] if x>0]

def readCulumn(Mat, i):
    return [x for x in Mat[0:, i] if x>0]

def readCase(Mat, i, j) :
    L =[]
    for x in range(3*(i//3), 3*(i//3)+3) :
        for y in range(3*(j//3), 3*(j//3)+3) :
            if (Mat[x,y] > 0) :
                L = L +[Mat[x,y]]
    return L

def conflits(Mat, i, j) :
    L = readLine(Mat,i)
    L = L + readCulumn(Mat,j)
    L = L + readCase(Mat,i,j)
    return set(L)

def sudoku(Mat) :
    global trouve
    cases = np.where(Mat==0)
    placer(Mat,cases,0)
    if (trouve): print(Mat)
    else : print("Il n'y a pas de solution")

def placer(Mat, cases, n) :
    global trouve
    if (n==len(cases[0])) : trouve=True ; return 
    valInterdites = conflits(Mat, cases[0][n],cases[1][n])
    for x in range(1,10):
        if not (x in valInterdites) :
            Mat[cases[0][n],cases[1][n]] = x
            placer(Mat, cases, n+1)
            if (trouve) : return
            Mat[cases[0][n],cases[1][n]] = 0

trouve=False
sudoku(Mat)
print(Mat)