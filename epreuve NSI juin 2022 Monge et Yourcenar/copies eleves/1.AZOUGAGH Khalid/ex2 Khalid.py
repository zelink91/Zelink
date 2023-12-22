# Créé par examen, le 01/06/2022 en Python 3.2
def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    if inverse == chaine:
        return True
    else:
        return False


def est_nbre_palindrome(nbre):
    chaine = est_palindrome(chaine)
    if chaine==nbre:
        return est_palindrome(chaine)

