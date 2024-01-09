# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:41:18 2021

@author: marce
"""
class File:
    ''' classe File
    création d'une instance File avec une liste
    '''
    def __init__(self):
        "Initialisation d'une file vide"
        self.L=[]

    def vide(self):
        "teste si la file est vide"
        return self.L==[]

    def defiler(self):
        "défile"
        assert not self.vide(),"Pile vide"
        return self.L.pop(0)

    def enfiler(self,x):
        "enfile"
        self.L.append(x)



class ArbreBinaire:
    """Structure de donnée d'arbre binaire

    Attributs
    ---------
    data: type simple int, float, str
        étiquette du nœud
    gauche: objet de type ArbreBinaire ou None si vide
        sous-arbre gauche
    droit: objet de type ArbreBinaire ou None si vide
        sous-arbre droit
    """

    def __init__(self, data, gauche=None, droit=None):
        self.data = data
        self.gauche =  gauche
        self.droit = droit

    # Méthode qui permet d’afficher la valeur
    # de la racine avec la fonction print
    def __str__(self):
        if self.data == None:
            return ""
        else:
            return str(self.data)

    def est_vide(self):
        if self.gauche==None and self.droit==None:
            return False
        else:
            return True

    def est_feuille(self):
        """
        EXERCICE 5
        une feuille n'a aucun fils droit ni gauche
        La fonction retourne True dans ce cas
        Sinon elle retourne vrai
        """
        if self.gauche==None and self.droit==None:
            return True
        else:
            return False

    # méthode hauteur de l'arbre
    def hauteur(self):
        """
        EXERCICE 6
        Calcul la hauteur d'un arbre, revient à parcourir l'arbre
        en retenant la plus grande profondeur rencontrée
        """
        if self.est_feuille()==True:
            return 0
        else:
            if self.gauche!=None and self.droit!=None:
                return (1 + max(self.droit.hauteur(),self.gauche.hauteur()))
            elif self.gauche!=None:
                return 1 +self.gauche.hauteur()
            else:
                return 1 +self.droit.hauteur()

    # méthode taille de l'arbre
    def taille(self):
        """
        EXERCICE 7
        Calcul la taille d'un arbre, c'est à dire le nombre de noeud
        """
        if self.est_feuille()==True:
            return 1
        else:
            if self.gauche!=None and self.droit!=None:
                return 1 + self.gauche.taille()+self.droit.taille()
            elif self.droit!=None:
                return 1 + self.droit.taille()
            else:
                return 1 + self.gauche.taille()

    def nb_feuille(self):
        """
        Exercice 8
        Compte uniquement les noeuds qui sont des feuilles
        """
        if self.est_feuille()==True:
            return 1
        else:
            if self.gauche!=None and self.droit!=None:
                return self.gauche.nb_feuille()+self.droit.nb_feuille()
            elif self.droit!=None:
                return self.droit.nb_feuille()
            else:
                return self.gauche.nb_feuille()





