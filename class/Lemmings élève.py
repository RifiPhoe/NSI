# -*- coding: utf-8 -*-
"""

@author: mperenno
"""
class Case:
    def __init__(self,char):
        self.terrain=char        
        self.lemming=None
        
    def __str__(self):
        if self.lemming!=None:
            return str(self.lemming)
        else:
            return str(self.terrain)        

        
    
class Jeu:
    def __init__(self,nomDeCarte):
        carte=open(nomDeCarte,"r")
        #permet d'initialiser chaque case du tableau à partir des éléments du fichier
        self.grotte=[[Case(char) for char in ligne if char!="\n"] 
                     for ligne in carte.readlines()]
        self.lemmings=[]
        
    def affiche(self):
        for ligne in self.grotte:
            for Case in ligne:
                print(Case, end ='')
            print()
        print("\n")

jeu=Jeu("map.txt")
jeu.affiche()