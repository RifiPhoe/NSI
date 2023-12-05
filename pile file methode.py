# EXO 1 PILE

'''def pile():
    # retourne une liste vide
    return[]

# vide
def vide(p):
    """Renvoie True si la pile est vide et False sinon"""
    return p==[]

# empiler
def empiler(p,x):
    """Ajoute l'élément x a la pile p"""
    p.append(x)

# depiler
def depiler(p):
    """Depile et renvoie l'element au sommet de la pile p"""
    assert not vide(p), "Pile vide"
    return p.pop()

# taille de la liste
def taille(p):
    return len(p)

# sommet de la liste
def sommet(p):
    return p[-1] # return p[len(p)-1]

p=pile()
for i in range(5):
    empiler(p,2*i)
a=depiler(p)
print(a)
print(vide(p))
print (sommet(p))'''

# EXO 2 PILE POO

class Pile :
    """Classe pile creation d'une instance Pile avec une liste"""

    def __init__(self):
        """initialisation d'une pile vide"""
        self.L=[]

    def vide(self):
        """teste si la pile est vide"""
        return self.L==[]

    def depiler(self):
        """depile"""
        assert not self.vide(), "Pile vide"
        return self.L.pop()

    def empiler(self,x):
        """empile"""
        self.L.append(x)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[len(self.L)-1]

'''p=Pile()
for i in range(5):
    p.empiler(2*i)
print(p.L)
a=p.depiler()
print(a)
print(p.L)
print(p.vide())
print(p.sommet())'''

# EXO 5 IMPLEMENTATION FILE METHODE 1

'''def file():
    #retourne une file vide
    return []

def vide(f):
    """renvoie True si la file est vide False sinon"""
    return f==[]

def enfiler(f,x):
    #ajoute x a la file f
    return f.append(x)

def defiler(f):
    #enleve et renvoie le premier element de la file
    assert not vide(f), "file vide"
    return f.pop(0)

def taille(f):
    return len(f)

def sommet(f):
    return f[0]

f=file()
for i in range(5):
    enfiler(f,2*1)
print(f)
a=defiler(f)
print(a)
print(f)
print(vide(f))
print(sommet(f))
print(taille(f))'''

# EXO 6 IMPLEMENTATION FILE METHODE 2

class File:
    """
    classe file creation d'une instance File avec une liste
    """

    def __init__(self):
        """Initialisation d'une file vide"""
        self.file = []

    def vide(self):
        """teste si la file est vide"""
        return self.file == []


    def defiler(self):
        """defile"""
        assert not self.vide(), "Pile vide"
        return self.file.pop()

    def enfiler(self,x):
        """enfile"""
        self.file.append(x)

    def taille(self):
        return len(self.file)

    def sommet(self):
        return self.file[0]

#CONTROLE PARENTHESAGE

'''def parentheses_controller(chaine:str)-> bool:
    parenthese = Pile()
    for lettre in chaine: # On recupere chaque lettre
        try:
            if lettre =="(": # Si c'est ouvrant -> tableau ajoute element
                parenthese.empiler(lettre)

            elif lettre ==")": # Fermant --> tableau enleve element
                parenthese.depiler()
        except:
            return False # Si une parenthese ouvrante manque (pas possible de depiler)
    if not parenthese.vide():# -> si le tableau n'est pas vide
        return False
    return True

print(parentheses_controller("(...(...)..."))'''
















