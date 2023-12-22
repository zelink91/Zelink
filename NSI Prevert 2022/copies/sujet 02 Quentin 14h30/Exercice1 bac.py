#Exercice1

def maxi (tab):
    elt=tab[0]
    cpt=0
    for i in range(len(tab)):
        if elt<tab[i]:
            elt=tab[i]
            cpt=i
    return elt,cpt
