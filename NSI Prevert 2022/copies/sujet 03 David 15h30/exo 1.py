# Créé par exam.NSI4, le 03/06/2022 en Python 3.7

def recherche (elt,tab):
    for i in range (len(tab)):
        if tab[i]==elt:
            return i
    return -1

