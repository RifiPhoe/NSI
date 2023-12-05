# EXO 1
class Tableau :
    def __init__(self):
        self.data=[]

    def longueur(self):
        return len(self.data)

    def est_vide(self):
        return not self.data

    def ajout(self,indice,valeur):
        self.data.insert(indice,valeur)

    def suppr(self,indice):
        self.data.pop(indice)

    def __repr__(self):
        return "Tableau ("+str(self.data)+")"