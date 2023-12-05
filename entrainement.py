def rechercheElement(tab, element):
    for el in tab:
        if el==element:
            return True
    return False

print(rechercheElement([1,3,2],3))

def recherchemax (tab):
    max=tab[0]
    for el in tab:
        if max<el:
            max=el
    return max
print(recherchemax([3]))

def calculsomme (tab):
    somme=tab[0]
    for el in tab:
        somme=somme+el
    return somme
print(calculsomme([7,8,9]))

