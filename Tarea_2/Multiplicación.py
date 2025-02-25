def multi(a, b):
    if b == 0:
        return 0
    if b > 0:  
        return a + multi(a, b - 1)
    return -multi(a, -b)

resultado = multi(7, 3) 
print(resultado)