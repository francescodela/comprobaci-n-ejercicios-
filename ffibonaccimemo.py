""" diccionario para almacenar ls resultados en fibonacci"""


memo = {}

def fibonacci (n):
    #si el resuktado ya esta en el diccionario ,retomarlo
    if n in memo :
        return memo [n]
    #caso base 
    if n == 0 :
        return 0 
    elif n == 1:
        return 1 
    #almacenar el resultado en el diccionario antes de retmarlo 
    memo [n]= fibonacci(n-1)+ fibonacci(n-2)
    return memo [n]
#ejemlo de uso 
print (fibonacci(10)) # da 55 