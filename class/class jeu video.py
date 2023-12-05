from random import *

class Personnage:
    """
    perso de jv
    """
    def __init__(self,genre,xp=0): # Constructeur
        self.genre = genre
        self.__xp = xp

    def get_xp(self): # retourne la valeur d'un attribut d'un objet
        return self.__xp

    def __set_xp(self,valeur): # Mutateur
        self.__xp = valeur

    def rencontre(self): # Fais evoluer l'xp de facon random a chaque rencontre
        n = randint(10,20) # tirage aléatoire entier entre 10 et 20
        self.__set_xp(self.get_xp()+n)

Peppa= Personnage("nb",0)
Peppa.rencontre()

print(Peppa.get_xp())

#print(Peppa.get_xp())

class Outil:
    def __init__(self,xp=8,masse=0,nbmains=1):
        self.xp = xp
        self.masse = masse
        self.nbmains = nbmains

    def mutation(self):
        if self.nbmains >1:
            self.nbmains -=1



Belier = Outil(20,25.89,4)
Stick = Outil(8,0.5,1)
Pickaxe = Outil(9,5.5,3)
Pickaxe.mutation()

#print(Pickaxe.nbmains)



