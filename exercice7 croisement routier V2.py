# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:14:29 2021

@author: marce
"""


def vide(f):
    ''' renvoie True si la file est vide False sinon'''
    return f==[]

def enfiler(f,x):
    #ajoute x à la file f"
    return f.append(x)

def defiler(f):
    #enlève et renvoie le premier élément de la file
    assert not vide(f), "file vide"
    return f.pop(0)

def sommet(f):
    return f[0]

def croisement(file1, file2):
    file3=[]
    while (vide(file1) != True) or (vide(file2)!= True):
        if (vide(file1) != True) and (vide(file2)!= True):
            if sommet(file1)==1 and sommet(file2)==2:
                enfiler(file3,1)
                defiler(file1)
            elif sommet(file1)==1 and sommet(file2)==0:
                enfiler(file3,1)
                defiler(file1)
            elif sommet(file1)==0 and sommet(file2)==2:
                enfiler(file3,2)
                defiler(file1)
                defiler(file2)
            else:
               enfiler(file3,0)
               defiler(file1)
               defiler(file2)
        elif (vide(file1) == True):
            enfiler(file3,sommet(file2))
            defiler(file2)
        else:
            enfiler(file3,sommet(file1))
            defiler(file1)

    return file3

f1=[0,1,1,0,1]
f2=[0,2,2,2,0,2,0]
f3=[]
print(croisement(f1,f2))



