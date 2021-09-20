# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:47:16 2021

@author: maelb
"""
from math import random

def plusoumoins(min:int,max:int):
    randomNomber = random.randint(min,max)
    # renvoie un entier entre min et max
    finduJeu = False
    coup = 0
    while not (finduJeu) and (coup < 11):
        monNbr = int(input("Entrez un nombre: "))
        if (monNbr > randomNomber):
            print("trop grand")
        elif (monNbr < randomNomber):
            print("trop petit")
        else:
            print("Tu gagnes en ", coup,"coup(s)")
            finduJeu = True
        coup += 1
    if (coup > 10):
        print("perdu")