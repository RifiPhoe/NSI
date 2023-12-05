

def division( n1, n2 ):
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
	    return quotient

# Programme principal
import doctest
doctest.testmod(verbose=True)	# exécution des test unitaires

