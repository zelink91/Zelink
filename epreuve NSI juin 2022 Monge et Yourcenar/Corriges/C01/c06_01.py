def maxi(tab):
    m = tab[0]
    indice = 0
    i = 0
    for v in tab:
        if v > m:
            m = v
            indice = i
        i = i + 1
    return (m,indice)
