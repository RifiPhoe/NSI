# exo 3

def miniLt(L):
    mini = L[0]
    for i in range (1, len(L)):
        mini = minimum(mini, L[i])
    return mini

def miniRec(L):
    if len(L)==1:
        return L[0]
    else:
        return minimum(L[0], miniRec(L[1:]))

def miniRec2(L):
    if len(L)== 1:
        return L[0]
    else:
        milieu=len(L)//2
        L1= L[0:milieu]
        L2= L[milieu:]
        return minimum(miniRec2(L1), miniRec2(L2))

# exo 1

liste=[8,5,7,9]
def sommeliste(liste):
    if len(liste)== 1:
        return liste[0]
    else:
        return liste[0]+sommeliste(liste[1:])