def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a >= 1 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a


print(binaire(0))
'0'
print(binaire(77))
'1001101'
