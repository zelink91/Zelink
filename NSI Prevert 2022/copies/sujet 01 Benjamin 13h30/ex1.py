def recherche(tab):
    L = []
    for i in range(1,len(tab)):
        if tab[i-1]+1 == tab[i]:
            L.append((tab[i-1],tab[i]))
    return L