import random

def algorithme_genetique():
    """Docstring zebi"""

    #Variables
    POIDS_SAC_MAX = 15
    compteur = 0

    while compteur < 2:
        prix = [4,4,3,3,5,5,3,3,5,6,6,5]
        poids = [5,7,2,2,6,8,3,4,9,11,8,7]
        taille_l = len(prix)
        genome = []
        for i in range(taille_l):
            genome.append(0)
        print(genome)

        somme_prix = 0
        somme_poids = 0

        while prix != [] and poids != []:
            taille_l = len(prix)

            print("Somme prix: ", somme_prix, "€. Somme poids: ", somme_poids)

            if somme_poids < POIDS_SAC_MAX:
                rand = random.randint(0, taille_l)
                if (somme_poids + poids[rand]) < POIDS_SAC_MAX:
                    print("Prix: ", prix[rand], "€. Poids: ", poids[rand], ".")
                    somme_prix = somme_prix + prix[rand]
                    somme_poids = somme_poids + poids[rand]
                    genome[rand] = 1
                    prix.pop(rand)
                    poids.pop(rand)
                else:
                    prix = []
                    poids = []
            else:
                prix = []
                poids = []

        print(genome)
        compteur += 1

algorithme_genetique()
