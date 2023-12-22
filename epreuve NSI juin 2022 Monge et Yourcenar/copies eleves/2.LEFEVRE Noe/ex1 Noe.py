

def maxi(tab):
    """
    la focntions maxi prend en parametre une liste tab de nombre entier et
    renvoie un couple donnant le plus grand element de cette liste ainsi que l'indice
    de la premiere apparitions de ce maxium
    """
    val_max = tab[0] # initialisations de la valeur max au debut de la liste
    indice_val_max = 0 #initialisations de l'indice de la valeur max a zero
    for ind in range(len(tab)):
        # print(ind) sert a voir l'interations de tab
        if val_max < tab[ind]:
            val_max = tab[ind]
            indice_val_max = ind
    return (val_max, indice_val_max)

print(maxi([1,5,6,9,1,2,3,7,9,8]))

# test additionelle
print(maxi([0]))
print(maxi([1,5,6,1,2,3,7,9,8]))