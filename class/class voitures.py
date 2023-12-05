class Voiture:
    # Attributs voiture
    def __init__ (self,couleur,vitesse):
        self.couleur = couleur
        self.vitesse = vitesse

    def rouler(self):
        pass
    def faire_le_plein(self, volume):
        pass

voit_jonathan = Voiture("rouge",30)
voit_denis = Voiture("grise",50)

print(voit_denis.couleur,voit_jonathan.couleur)
