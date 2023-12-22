# Créé par examen, le 01/06/2022 en Python 3.2
def recherche(elt,tab):
    l=[]
    for i in range(len(tab)):
        if tab[i]==elt:
            l.append(i)
    return l
