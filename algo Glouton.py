differentes_monnaies = [50,20,10,5,2,1]

def algoGlouton(somme):
    monnaie = []
    somme_restante = somme
    while somme_restante > 0:
        for une_monnaie in differentes_monnaies:
            if une_monnaie <= somme_restante:
                monnaie.append(une_monnaie)
                somme_restante -= une_monnaie
                break
    return monnaie
print(algoGlouton(4))