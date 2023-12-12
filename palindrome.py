# itératif

def est_palindrome(mot):
    mot = mot.lower()
    for i in range(len(mot)//2):
        if mot[i] != mot[-i-1]:
            return False
        return True




def est_palindromer(mot):
    if len(mot) < 2 :
        return True
    if mot[0] != mot[len(mot)-1]:
        return False
    return (est_palindromer(mot[1:-1]))
