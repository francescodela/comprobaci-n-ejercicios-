def factorial (n):
    #caso base ; si n es 0 , retorna 1 
    if n == 1:
        return 1 
    # llamada recursiva : n * factorial (n-1)
    else : 
        return n *  factorial (n-1)
# ejemplo de uso 
print (factorial(5)) # da 120 