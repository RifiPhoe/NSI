from random import *
from outil import *
class PersonnageAvecOutil:
    """
    perso de jv
    """
    def __init__(self,genre,xp=0): # Constructeur
        self.genre = genre
        self.__xp = xp
        self.objet = Outil(0,0.5) # (ligne ajoutee)

    def get_xp(self): # retourne la valeur d'un attribut d'un objet
        return self.__xp

    def __set_xp(self,valeur): # Mutateur
        self.__xp = valeur

    def rencontre(self): # Fais evoluer l'xp de facon random a chaque rencontre
        n = randint(10,20) # tirage aléatoire entier entre 10 et 20
        self.__set_xp(self.get_xp()+n)

    def get_objet(self): # Methode faisant appel à la classe Outil
        """accesseur des caracteristiques masse et nombre de mains de l'objet"""
        masse = self.objet.get_masse()
        main = self.objet.get_main()
        return masse,main


    def decouverte(self,xp,masse,main):
        if self.__xp<xp:
            self.objet=Outil(8,1.23,2)
            print("Nouvel objet")
        else:
            print("Dommage, il faut encore progresser en niveau")


#def decouverte(self,xp=,masse=0,main=1):
       # xp = self.get_xp()
       # masse = self.objet.get_masse()
       # main = self.objet.get_main()
        #if decouverte(8,0,1)>=get_objet():
            #print("Nouvel objet")
        #else:
            #print("Dommage, il faut encore progresser en niveau")



