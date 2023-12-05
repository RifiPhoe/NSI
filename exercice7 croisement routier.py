# -*- coding: utf-8 -*-

class File:
    ''' classe File
    création d'une instance File avec une liste
    '''
    def __init__(self,liste=[]):
        "Initialisation d'une file vide"
        self.L=liste

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

    def sommet(self):
        return (self.L[0])

def croisement(file1, file2):
    file3=File()
    while (file1.vide() != True) or (file2.vide()!= True):
        if (file1.vide() != True) and (file2.vide()!= True):
            if file1.sommet()==1 and file2.sommet()==2:
                file3.enfiler(1)
                file1.defiler()
            elif file1.sommet()==1 and file2.sommet()==0:
                file3.enfiler(1)
                file1.defiler()
            elif file1.sommet()==0 and file2.sommet()==2:
                file3.enfiler(2)
                file1.defiler()
                file2.defiler()
            else:
               file3.enfiler(0)
               file1.defiler()
               file2.defiler()
        elif (file1.vide() == True):
            file3.enfiler(file2.sommet())
            file2.defiler()
        else:
            file3.enfiler(file1.sommet())
            file1.defiler()


    return file3
f1=File([0,1,1,0,1])
f2=File([0,2,2,2,0,2,0])
f3=File()
f3=croisement(f1,f2)
print(f3.L)

