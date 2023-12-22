# Créé par examen, le 01/06/2022 en Python 3.2
def recherche(elt,tab):
    for i in range(len(tab)):
        if elt == tab[i]:
            return i
    return -1
print(recherche(1,[5,5,7]))

