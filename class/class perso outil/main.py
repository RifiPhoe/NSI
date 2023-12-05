from personnage_avec_outil import *
# importation de personnage_avec_outil.py

# gestion de l'affichage de la saisie du genre par l'utilisateur
genre = input("""
            Saisir la lettre correspondante au genre desire pour votre personnage :
                M : si vous voulez un heros de genre masculin,
                F : si vous voulez une heroine de genre feminin,
                A : si vous voulez un personnage sans genre détermine
            """)

genre = genre.upper() # pour s'assurer que la lettre saisie est en majuscule

# creation du nouveau personnage, appele ici par defaut hero
if genre=="F":
    hero = PersonnageAvecOutil("Feminin")
elif genre=="M":
    hero = PersonnageAvecOutil("Masculin")
elif genre=="A":
    hero = PersonnageAvecOutil("Autre")
else:
    print("Erreur de saisie dans le choix du genre.")

# Affichage d'une caracteristique du personnage cree :
print("Votre personnage a comme niveau d'experience {}.".format(hero.get_xp()))
# Decouverte des caracteristiques de l'objet en main du heros ou de l'heroine :
print("Vous commencez avec un baton de marche de masse {} que vous pouvez tenir a {}.".format(hero.get_objet()[0],hero.get_objet()[1]))