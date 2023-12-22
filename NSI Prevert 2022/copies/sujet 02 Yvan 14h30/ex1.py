def maxi(tab):
    a=0
    cpt=0
    for i in range (len(tab)):
        if a<tab[i]:
            a=tab[i]
            cpt=i
    return a,cpt