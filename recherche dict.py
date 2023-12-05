# Créé par marce, le 29/10/2022 en Python 3.4


def plus_grand_nombre(zoo):
    """
    Retourne le nom de l’animal le plus représenté dans le zoo.
    """
    nbre_max = 0  # nbre maximale d'animaux
    for (cle, valeur) in zoo.items():
        if valeur[1] > nbre_max:
            nbre_max = valeur[1]
            cle_max = cle
        elif valeur[1] == nbre_max:
            cle_max += ", " + cle
    print(cle_max)
    return cle_max


def nbre_total_continent(zoo,continent):
    """
    Retourne le nombre d’animaux originaires de ce continent dans le zoo.
    """
    nbre_total = 0  # Nbre total d'animaux pour le continent
    for valeur in zoo.values():
        if valeur[0] == continent:
            nbre_total += valeur[1]
    print(nbre_total)
    return nbre_total


def nbre_pour_animal(zoo,animal):
    """
    Retourne le nombre de représentants de animal dans zoo.
    """
    if animal in zoo.keys():
        rep = zoo[animal][1]
    else:  # si animal pas présent dans zoo
        rep = 0
    return rep


zoo_Beauval = {
    'éléphant': ('Asie', 5),
    'écureuil': ('Asie', 17),
    'panda': ('Asie', 2),
    'hippopotame': ('Afrique', 7),
    'girafe': ('Afrique', 4),
    'lion': ('Afrique', 17)
    }

zoo_LaFleche = {
    'ours': ('Europe', 4),
    'tigre': ('Asie', 7),
    'girafe': ('Afrique', 11),
    'hippopotame': ('Afrique', 3)
    }

assert plus_grand_nombre(zoo_LaFleche) == 'girafe'
assert plus_grand_nombre(zoo_Beauval) == 'écureuil, lion' or 'lion, écureuil'

assert nbre_total_continent(zoo_LaFleche, 'Afrique') == 14
assert nbre_total_continent(zoo_Beauval, 'Asie') == 24

assert nbre_pour_animal(zoo_Beauval, 'panda') == 2
assert nbre_pour_animal(zoo_LaFleche, 'panda') == 0