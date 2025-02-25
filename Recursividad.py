#numero=6
#resultado:int

#def factorial (n:int)->int:
    #res:int=1
    #contador=0
    #while contador <=n:
        #res=res*contador
        #contador=contador+1
    #return



numero=5

def factorial (n:int)-> int:
    if n==1:
        return n
    factorial(n-1)*n
    print(factorial(numero))