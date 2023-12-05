# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:45:35 2023

@author: mperenno
"""
import random

def tri_insertion(tab):
    """
    Donnée : prend un tableau tab de longeur n
    Résultat : renvoie le tableau trié par ordre croissant
    """
    for i in range(1 , len(tab)):
        #sélection de chaque élément
        a_inserer = tab[i]
        j = i
        while j > 0 and tab[j - 1] > a_inserer:
            #insertion de l'élément à sa place par décalage
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = a_inserer
    return tab

def tri_selection(tab):
    """
    Donnée : prend un tableau tab de longeur n
    Résultat : renvoie le tableau trié par ordre croissant
    """    
    for i in range(0,len(tab)) :
        #sélection de chaque élément
        indexMin = i
        for j in range(i+1, len(tab)) :
            #recherche d'un minimum dans le reste de la liste
            if tab[j] < tab[indexMin] :
                indexMin = j
        if indexMin != i :
            #inversion des éléments
            number = tab[i]
            tab[i] = tab[indexMin]
            tab[indexMin] = number
    return tab  

tab=[13,45,20]
print(tri_insertion(tab))

tab=[13,45,20]
print(tri_selection(tab))

tab = [random.randrange(0,100) for i in range(10)]
print(tri_selection(tab))