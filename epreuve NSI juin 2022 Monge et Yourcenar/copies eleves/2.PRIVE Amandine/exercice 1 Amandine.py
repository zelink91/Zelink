# Créé par examen, le 01/06/2022 en Python 3.2
def maxi(tab):
    maximum = 0
    indice = 0
    for i in range(len(tab)):
        if tab[i]>maximum:
            maximum = tab[i]
            indice = i
    return maximum,indice


