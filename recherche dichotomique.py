# tab doit être un tableau trié
def recherche_dichotomique(tab,val):
    gauche = 0
    droite = len(tab) - 1
    while gauche<=droite:
        milieu = (gauche+droite)//2
        if tab[milieu] == val:
            #on a trouve val dans le tableau
            # a la position du milieu
            return milieu
        elif tab[milieu] > val:
            # on cherche entre gauche et milieu - 1
            droite = milieu - 1
        else:
            # on a tab[milieu] < val
            # on cherche entre milieu +1 et droite
            gauche = milieu + 1
        # on est sorti de la boucle sans trouver val
    return -1
print(recherche_dichotomique([4,5,6,7,22],4))
