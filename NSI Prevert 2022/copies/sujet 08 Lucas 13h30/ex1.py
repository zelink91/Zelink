def multiplication(n1,n2):
    resultat = 0
    if n1 > 0 and n2> 0:
        for i in range(n1):
            resultat = resultat + n2
    elif n1 > 0 and n2 < 0 :
        for i in range(n1):
            resultat = resultat + n2
    elif n1 < 0 and n2> 0 :
        for i in range(n2):
            resultat = resultat + n1
    else :
        for i in range(abs(n1)):
            resultat = resultat + abs(n2)
    return resultat


