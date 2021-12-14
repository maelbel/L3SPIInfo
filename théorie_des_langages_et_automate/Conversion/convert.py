def convert(nombre:int, base:int)-> str:
    """Fonction qui transforme base 10 en base autre"""

    #variables
    message = ""
    compteur = 0
    puissance = base**compteur

    while puissance < nombre:
        compteur += 1
        puissance = base**compteur
        print(puissance)

    while compteur != -1:
        if puissance > nombre:
            message += "0"
        else:
            message += "1"
            nombre = nombre - puissance
        compteur -= 1
        puissance = base**compteur

    return message
print(convert(1789, 2))
