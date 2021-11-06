# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:09:40 2021

@author: maelb
"""

def somme(N):
    if N > 0:
        return N+somme(N-1)
    else:
        return 0
print(somme(9))

def contientZero(N):
    if(N<10):
        return N == 0
    elif(N%10 == 0):
        return True
    else:
        contientZero(N//10)

print(contientZero(10050))

def puissance(x, n):
    if(n == 1):
        return x
    else:
        p = puissance(x, n//2)
        if(n%2 == 0):
            return p*p
        else:
            return p*p*x

print(puissance(2, 10))

T = [4,8,6,3,2]

def distance(x, d, f):
    if(f == d):
        return x - T[d]
    else:
        min(x-T[d], distance(x, d+1, f))

print(distance(6, 1, len(T)))

def fibonacci():
    return 0