def chercher(T,n,i,j):

    if i < 0 or j > len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, m , j)
    elif T[m] > n :
        return chercher(T, n, i , m )
    else :
        return m
