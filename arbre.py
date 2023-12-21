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
    
    def hauteur(self,noeud):
        if self.est_feuille == True:
            return -1
        else:
            




def affiche(arbre):
   if arbre!= None:
      return (arbre.data,affiche(arbre.gauche),affiche(arbre.droit))

ng = ArbreBinaire(9)
nd = ArbreBinaire(4)
ng = ArbreBinaire(1, ng, nd)
nd = ArbreBinaire(12)
nd = ArbreBinaire(6, ng, nd)
ngd = ArbreBinaire(3)
ng = ArbreBinaire(10, droit = ngd)

arbre = ArbreBinaire(5, ng, nd)

print ("racine",arbre) #affiche la racine de l'arbre
print(affiche(arbre))

ng=None
nd=None
nd=ArbreBinaire("C")
ngg=ArbreBinaire("B",droit=nd)
nd=ArbreBinaire("D")
arbre2 = ArbreBinaire("A",ngg,nd)
print("racine",arbre2)
print(affiche(arbre2))

