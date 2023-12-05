# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:46:19 2021

@author: resptechno
"""
class Tableau:
    """
    tableau sur une plage d'indice qcq
    """
    def __init__(self,imin,imax,v):
        self.premier=imin
        #self.contenu=[v] * (imax-imin + 1)
        self.contenu=[]
        for i in range (imax-imin+1):
            self.contenu.append(v)
       
    def __len__(self):
        return len(self.contenu)
    
    def __getitem__(self,i):
        return self.contenu[i-self.premier]
    
    def __setitem__(self,i,v):
        if i>self.premier-1 and i<len(self.contenu)+self.premier:
            self.contenu[i-self.premier]=v
        else:
            raise IndexError("l'indice est en dehors de la plage")
    
    def __str__(self):
        return str(self.contenu)
            
        
#construction d'un tableau de 20 éléments initialisés à la valeur 42       
tableau=Tableau(-10,9,42)
#modifie l'élement d'indice 12 dans le tableau
tableau[2]=20
print(tableau)
print(len(tableau))
tableau[-10]=20
print(tableau)       