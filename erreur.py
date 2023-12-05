from timeit import timeit
#import doctest


# EXO 1

'''def inverse(n):
    assert n != 0, "Le nombre ne doit pas être nul."
    assert n > 0, "Le nombre doit être positif."
    assert isinstance(n,int), "Le nombre doit être un entier."

inverse((1.2))'''

# EXO 2

'''def minimumListe (lst):
    assert isinstance(lst,list), "La fonction attend une liste."
    longueur=len(lst)
    assert longueur>0,"La liste doit etre superieure a zero."
    mini=lst[0]
    i=1
    while (i<longueur):
        if lst[i]<mini:
            mini = lst[i]
        i+=1
    return mini

print(minimumListe([3,5]))'''

# EXO3 3

'''def affichageInverse(lst):
    for x in lst:
        print(x, end=",")
        try:
            print(1.0/x)
        except ZeroDivisionError:
            print("N'admet pas d'inverse")
        except TypeError:
            print("calcul d'inverse uniquement pour des nombres (int ou float)")

lstNombres=[0.3333,2.5,0,10]
affichageInverse(lstNombres)
lstNombres = [0.3333,2.5,0,10]
affichageInverse(lstNombres)'''

# EXO 4

'''def ouvertureFichierLecture(nomfic):
    erreur=""
    f=None
    try:
        f=open(nomfic,"r")
    except FileNotFoundError:
        erreur="le fichier " + nomfic + " est introuvable"
    return f,erreur

fic, err = ouvertureFichierLecture("test.txt")
if err!="":
    print(err)'''

# DOCTEST

'''def division( n1, n2 ):
	    """
	    	Fonction pour calculer le quotient et le reste de la division de deux nombres.

	    	Entrée :
	        deux nombres n1, n2
	    	Sortie :
	        deux entiers dans l'ordre : quotient, reste de la division de n1 par n2

	    Tests unitaires :
	    >>> division(1,1)
	    (1, 0)

	    >>> division(2,1)
	    (2, 0)

	    >>> division(10,3)
	    (3, 1)
	    """

	    quotient = n1 // n2
	    reste = n1 % n2
	    return quotient, reste

# Programme principal

doctest.testmod()	# exécution des test unitaires'''

# EXO TIMEIT

def test(n):
    """Fonction inutile"""
    n = n*n

t = timeit(stmt = 'test(1000)', setup="from erreur import test", number = 100)
print(t)


