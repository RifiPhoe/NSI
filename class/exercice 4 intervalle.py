# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:18:52 2021

@author: resptechno
"""
class Intervalle:
    """
    classe pour représenter un intervalle fermé 
    d'extrémité a et .
    l'intervalle est vide si b<a 
    """
    def __init__(self,a,b):
        self.a=a
        self.b=b
            
    def est_vide(self):
        vide = False
        if self.b<self.a:
            vide=True
        return vide
            
    def __len__(self):
        if self.est_vide()==True:
            return 0
        else:
            return self.b-self.a
            
    def __contains__(self,x):
        appartient=False
        if x>=self.a and x<=self.b:
            appartient=True
        return appartient
            
    def __eq__(self,interv):       
        egal=False
        if self.a==interv.a and self.b==interv.b:
            egal=True
        return egal
    
    def intersection(self, interv2):
        return Intervalle(max(self.a,interv2.a),min(self.b,interv2.b))
    
    def union(self, interv2):
        return Intervalle(min(self.a,interv2.a), max(self.b,interv2.b))
         