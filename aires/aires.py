# Importe le module pi de math
from math import pi
"""
Fourniture de fonctions calculant les surfaces de diverses figures géométriques : disque, rectangle et triangle.
"""

def disque(rayon:float):
    r = rayon**2*pi
    return r

def rectangle(largeur:float, longueur:float):
    aire = largeur*longueur
    return aire

def triangle(base:float,hauteur:float):
    aire = base*hauteur/2
    return aire

print(triangle(6.8,8.9))

