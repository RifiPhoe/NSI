class Point:
    # Une classe pour représenter un point à partir de ses coordonnées
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def deplace(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

# p est une instance de la classe Point
p = Point(2,3)
# r est une autre instance de la classe Point
r = Point(-1,3)
print(p,r)

# Accès aux attributs d'un objet : objet.attribut
print("Abscisse de p :", p.x)
print("Ordonnée de p :", p.y)
