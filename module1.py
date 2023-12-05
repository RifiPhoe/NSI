class Cellule:
    def __init__(self,valeur=None,suivant=None):
        """
        Paramètres
        ----------
        valeur : type quelconque
        Description : Une valeur stockée dans la cellule
        suivant : Un autre objet de type “Cellule”
        Description : La cellule qui “suit” cette cellule selon l’ordre
        défini par la structure.
        ----------
        Crée une cellule avec une valeur et l’adresse de la cellule qui la suit.
        """
        self.valeur = valeur
        self.suivant = suivant # si suivant = None : Pas de cellule suivant

    def __str__(self):
        if self.suivant==None:
            Macellule = str(self.valeur) + "-> None"
        else:
            Macellule = str(self.valeur) + "-> " + str(self.suivant)
        return Macellule



class ListeC:
    def __init__(self):
        """
        Crée une liste vide.
        l'attribut tête est un objet cellule qui définit la cellule
        en tête de liste (premier élément de la liste)
        """
        self.tete = None # Liste vide

    def __str__(self):
        return str(self.tete)

    def est_vide(self):
        return L.tete is None

    def tailleListe(self):
        """ Renvoie le nombre de Maillons de la liste L """
        l = 0
        elt = self.tete

        while elt.suivant != None:
            l = l + 1
            elt = elt.suivant

        return l

    def get_dernier_maillon(self):
        elt = self.tete
        while elt.suivant != None:
                elt = elt.suivant

        return elt


    def get_maillon_indice(self, i):
        """ Renvoie Maillon d'indice i dans la liste L """
        j = 0
        m = self.tete

        while j < i:
            j+= 1
            m = m.suivant

        return m



    def ajouter_debut(self, nM):
        """ Ajoute le maillon nM en tête de la liste L """
        elt = self.tete
        maillon = Cellule(nM,elt)
        self.tete = maillon



    def ajouter_fin(self, nM):
        """ Ajoute le maillon nM en queue de la liste L """

        m = self.tete
        while m.suivant is not None :
            m = m.suivant
        m.suivant = nM


    def supprimer_fin(self):
        """ Supprime le dernier maillon de la liste L et le renvoie """

        m = self.tete
        while m.suivant.suivant is not None:
            m = m.suivant
        m.suivant = None
        return m

    def inserer(self, M, nM):
        """ Ajoute le maillon M après celui d'indice i dans la liste L """
        nM.suivant = M.suivant
        M.suivant = nM



L = ListeC()
M1, M2 = Cellule(21), Cellule(15)
M1.suivant = M2
L.tete = M1
print(L)

print(L.tailleListe())
print(L.get_maillon_indice(1))

M3=Cellule(45)
L.ajouter_fin(M3)
print(L)

M4=Cellule(37)
L.inserer(M1,M4)
print(L)