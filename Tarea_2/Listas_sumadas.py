def suma (arreglo): 
    if not arreglo :  
        return 0  
    return arreglo [0]+ suma (arreglo[1:]) 

numeros =[1,2,3,4,5]
print (suma(numeros))