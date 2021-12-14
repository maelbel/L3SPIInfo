# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:51:06 2021

@author: maelb
"""
def MER (m, n):
    return MERAUX(m, n, 0)

def MERAUX(m, n, p):
    if(n==0): 
        return p
    elif (n%2==0):
        return MERAUX(2*m, n/2, p)
    else:
        return MERAUX(2*m, n//2, m+p)
    
print(MER(12,9))

def MERI(m, n):
    p = 0
    
    while(n > 0):
        if(n%2 != 0): p = p + m 
        m = m * 2
        n = n // 2
    
    return p

print(MERI(12,9))