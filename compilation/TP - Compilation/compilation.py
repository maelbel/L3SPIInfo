#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:01:41 2021

@author: m b
"""

def ADD(pile:list)->None:
    """Fonction qui additionne le sous-sommet de pile au sommet, laisse le résultat au sommet

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    pile[taille] = pile[taille-1] + pile[taille]


def SUB(pile:list)->None:
    """Fonction qui soustrait le sous-sommet de pile au sommet, laisse le résultat au sommet

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    pile[taille] = pile[taille-1] - pile[taille]


def MUL(pile:list)->None:
    """Fonction qui multiplie le sous-sommet de pile au sommet, laisse le résultat au sommet

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    pile[taille] = pile[taille-1] * pile[taille]


def DIV(pile:list)->None:
    """Fonction qui divise le sous-sommet de pile au sommet, laisse le résultat au sommet

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    pile[taille] = pile[taille-1] / pile[taille]


def EQL(pile:list)->None:
    """Fonction qui laisse 1 au sommet de pile si sous-sommet = sommet, 0 sinon

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    if(pile[taille-1] == pile[taille]):
        pile[taille] = 1
    else:
        pile[taille] = 0


def NEQ(pile:list)->None:
    """Fonction qui laisse 1 au sommet de pile si sous-sommet < sommet, 0 sinon

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    if(pile[taille-1] != pile[taille]):
        pile[taille] = 1
    else:
        pile[taille] = 0


def GTR(pile:list)->None:
    """Fonction qui laisse 1 au sommet de pile si sous-sommet > sommet, 0 sinon

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    if(pile[taille-1] > pile[taille]):
        pile[taille] = 1
    else:
        pile[taille] = 0



def LSS(pile:list)->None:
    """Fonction qui laisse 1 au sommet de pile si sous-sommet < sommet, 0 sinon

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    if(pile[taille-1] < pile[taille]):
        pile[taille] = 1
    else:
        pile[taille] = 0

def GEQ(pile:list)->None:
    """Fonction qui laisse 1 au sommet de pile si sous-sommet >= sommet, 0 sinon

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    if(pile[taille-1] >= pile[taille]):
        pile[taille] = 1
    else:
        pile[taille] = 0

def LEQ(pile:list)->None:
    """Fonction qui laisse 1 au sommet de pile si sous-sommet <= sommet, 0 sinon

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    if(pile[taille-1] <= pile[taille]):
        pile[taille] = 1
    else:
        pile[taille] = 0

def PRN(pile:list)->None:
    """Fonction qui imprime le sommet, dépile

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    print(pile[taille])
    pile.pop(taille)


def INN(pile:list)->None:
    """Fonction qui lit un entier, le stocke à l'adresse trouvée au sommet de pile, dépile

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    inner = int(input("Veuillez saisir un entier: "))
    sp = pile[taille]
    pile[sp] = inner
    pile.pop(-1)

def INT(sp:int, c:int)->int:
    """Fonction qui incrémente de la constante c le pointeur de pile (la constante c peut être négative)

    inputs:
        int sp : Pointeur de Pile
        int c : Constance c

    outputs:
        int: Addition de sp + c"""

    return sp + c

def LDI(pile:list, v:int)->None:
    """Fonction qui empile la valeur v

    inputs:
        list pile : pile mémoire
        int v : valeur a empiler

    outputs:
        None"""

    pile.append(v)

def LDA(pile:list, a:int)->None:
    """Fonction qui empile l'adresse a

    inputs:
        list pile : pile mémoire
        int a : adresse à empiler

    outputs:
        None"""

    pile.append(a)

def LDV(pile:list)->None:
    """Fonction qui remplace le sommet par la valeur trouvée à l'adresse indiquée par le sommet (déréférence)

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    sp = pile[taille]
    pile[taille] = pile[sp]

def STO(pile:list)->None:
    """Fonction qui stocke la valeur au sommet à l'adresse indiquée par le sous-sommet, dépile 2 fois

    inputs:
        list pile : pile mémoire

    outputs:
        None"""

    taille = len(pile)-1
    sp = pile[taille-1]
    pile[sp] = pile[taille]

    pile.pop(-1)
    pile.pop(-1)

def BRN(i:int)->None:
    """branchement inconditionnel à l'instruction i

    inputs:
        int i : instruction n°i

    outputs:
        int : retourne l'instruction i """

    return i

def BZE(pile:list, i:int)->int:
    """branchement à l'instruction i si le sommet = 0, dépile

    inputs:
        list pile : pile mémoire
        int i : instruction n°i

    outputs:
        int : retourne l'instruction i """

    taille = len(pile)-1

    if pile[taille]==0:
        return i

    pile.pop(-1)



def HLT()->None:
    """Fonction qui halte"""
    print("Halte là !")

def ERR()->None:
    """Fonction qui affiche une erreur"""
    print("Error: Invalid Syntax")


PCODE = [
    ["LDI", 5],
    ["LDA", 3],
    ["LDI", 6],
    ["LDI", 0],
    "ADD",
    "EQL",
    "INN",
    ["INT", 2],
    ["LDI", 0],
    ["BZE", 10],
    "ADD",
    "SUB",
    ["LDA", 3],
    "LDV",
    ["LDA", 1],
    ["LDI", 5],
    "STO",
    ["BRN", 18],
    "PRN",
    "PRN",
    "HLT"]


def interpreteur():

    mem = []
    sp = 0
    pc = 0
    INST = ""

    while PCODE[pc] != "HLT":

        sp = len(mem)-1

        if PCODE[pc] == "ADD":
            INST = PCODE[pc]
            ADD(mem)
        elif PCODE[pc] == "SUB":
            INST = PCODE[pc]
            SUB(mem)
        elif PCODE[pc] == "MUL":
            INST = PCODE[pc]
            MUL(mem)
        elif PCODE[pc] == "DIV":
            INST = PCODE[pc]
            DIV(mem)

        elif PCODE[pc] == "EQL":
            INST = PCODE[pc]
            EQL(mem)
        elif PCODE[pc] == "NEQ":
            INST = PCODE[pc]
            NEQ(mem)
        elif PCODE[pc] == "GTR":
            INST = PCODE[pc]
            GTR(mem)
        elif PCODE[pc] == "LSS":
            INST = PCODE[pc]
            LSS(mem)
        elif PCODE[pc] == "GEQ":
            INST = PCODE[pc]
            GEQ(mem)
        elif PCODE[pc] == "LEQ":
            INST = PCODE[pc]
            LEQ(mem)

        elif PCODE[pc] == "PRN":
            INST = PCODE[pc]
            PRN(mem)

        elif PCODE[pc] == "INN":
            INST = PCODE[pc]
            INN(mem)

        elif PCODE[pc][0] == "INT":
            INST = PCODE[pc][0]
            mem[sp] = INT(mem[sp], PCODE[pc][1])

        elif PCODE[pc][0] == "LDI":
            INST = PCODE[pc][0]
            LDI(mem, PCODE[pc][1])

        elif PCODE[pc][0] == "LDA":
            INST = PCODE[pc][0]
            LDA(mem, PCODE[pc][1])

        elif PCODE[pc] == "LDV":
            INST = PCODE[pc]
            LDV(mem)

        elif PCODE[pc] == "STO":
            INST = PCODE[pc]
            STO(mem)

        elif PCODE[pc][0] == "BRN":
            INST = PCODE[pc][0]
            pc = BRN(PCODE[pc][1])

        elif PCODE[pc][0] == "BZE":
            INST = PCODE[pc][0]
            pc = BZE(mem, PCODE[pc][1])

        else:
            ERR()

        print(INST)
        pc += 1

    HLT()

interpreteur()
