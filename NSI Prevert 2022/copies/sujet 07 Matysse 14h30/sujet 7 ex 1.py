def maxi(tab):
    a=0
    b=0
    for i in range(len(tab)-1):
        if tab[i]<tab[i+1]:
            a+=1
            b=tab[i+1]

    return (b,a)






