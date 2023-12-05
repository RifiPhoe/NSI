from random import randint

L=[randint(0,100) for i in range(20)]

# Exercice 1
def somme(L: list) -> int:
    """Fonction qui renvoie la somme d'une liste de nombre"""
    total = 0
    for nombre in L: # on vient rÃƒÂ©cuperer chaque nombre de la liste
        total += nombre # on addition avec le nombre rÃƒÂ©cupÃƒÂ©rer
    return total


# Exercice 2
def maxi(L: list) -> int:
    """Fonction qui renvoi le nombre maximum d'une liste de nombre"""
    maximum = L[0]
    for nombre in L: # On rÃƒÂ©cupÃƒÂ¨re chaque nombre de L
        if maximum < nombre: # On regarde si L est plus grand que maximum
            maximum = nombre # On attribut nombre ÃƒÂ  maximum si plus grand
    return maximum


# Exercice 3
def puissance(x: int,n: int) -> int:
    """Fonction qui renvoie x puissance n"""
    return x**n # ** permet de faire une puissance

# Exercice 4
def compare(l1: list,l2: list) -> list:
    """Fonction qui compare deux liste et renvoie les
    nombres qu'elles ont en commun"""
    nombre=[]
    for i in l1: # On vient chercher chaque ÃƒÂ©lÃƒÂ©ment de la liste 1
        if i in l2: # si l'ÃƒÂ©lÃƒÂ©ment de la liste 1 est dans la liste 2
            nombre.append(i) # On l'ajoute ÃƒÂ  la variable nombre
    return nombre


# Exercice 5
def inverse(mot: str) -> str:
    """Fonction qui renvoie le mot saisie ÃƒÆ’Ã‚Â  l'envers"""
    motInverse = ""
    for i in range(1,len(mot) + 1): # on vient chercher chaque index du mot
        motInverse += mot[0-i] # on ajoute les lettres de faÃ§on inversÃ©
    return motInverse


# Exercice 6
def demontrerInverse(mot: str) -> bool:
    """Fonction qui renvoi un boolean si le mot est un palindrome ou non"""
    return inverse(mot) == mot # On regarde si l'inverse de mot est Ã©gal Ã  mot


# Exercice 8
def Fibonacci () -> list:
    """Renvoi les 10 premiers chiffres de la suite de Fibonacci"""
    suite = [0,1]
    n=1
    for _ in range(8):
        nombre = suite[n] + suite[n-1] # Loi de Fibonacci
        suite.append(nombre) # On ajoute le nombre de la suite
        n+=1
    return suite

# Exercice 3 (variante)
def puissanceVariante(x: int,n: int) -> int:
    """Fonction qui effectue x puissance n avec un boucle for"""
    if n == 0: # Si une puissance est ÃƒÂ©gal ÃƒÂ  0, le nombre c'est 1
        return 1
    total = x
    for _ in range(n-1):
        total = total * x # On multiplie le nombre
    return total

# Exercice 4 (variante)
def compareVariant(l1: list,l2: list) -> str:
    """Compare deux liste"""
    for nombreL1 in l1:
        for nombreL2 in l2:
            if nombreL1 == nombreL2:
                return "Il y a une correspondance."
    return "Aucune correspondance"



########################
###       TEST       ###
########################

# La liste
print("La liste: ", L)

# Exercice 1
print("Fonction somme: ", somme(L))

# Exercice 2
print("Fonction maximum: ", maxi(L))

# Exercice 3
print("Fonction puissance: ", puissance(5,3))

# Exercice 3 (Variant)
print("Fonction puissance (variant): ", puissanceVariante(5,3))

# Exercice 4
print("Fonction compare: ", compare([1,2,3,4,5],[9,8,5,2]))

# Exercice 4 (Variant)
print("Fonction compare (variant): ", compareVariant([1,2,3,4,5],[9,8,5,2]))

# Exercice 5
print("Fonction inverse: ", inverse("mayonnaise"))

# Exercice 6
print("Fonction demontrerInverse: ", demontrerInverse("kayak"))

# Exercice 8
print("Fonction Fibonacci: ", Fibonacci())

# --------------------------------------------------------------------- #