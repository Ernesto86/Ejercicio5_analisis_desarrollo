from math import sqrt
def get_ListaFibonacci(n):
    lista = [0, 1]
    for i in range(3, n):
        lista.append(lista[len(lista) - 1] + lista[len(lista) - 2])
    return lista

def get_Divisores(n):
    divs = {1,n}
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            divs.update((i,n//i))
    return divs

def encontrar_divisor_mayor_mil(fibonaccis):
    constante = 12
    contador = 0
    data = {"fibonacci": 0,"divisores": {}}
    for i in range(0, int(len(fibonaccis)/constante)):
        contador = contador + constante
        fib = fibonaccis[contador]
        divisores = get_Divisores(fib)
        if len(list(divisores)) >= 1000:
            data["fibonacci"] = fib
            data["divisores"] = divisores
            return data
    return data

fibonaccis = get_ListaFibonacci(100)
data = encontrar_divisor_mayor_mil(fibonaccis)
print('Fibonacci: ',data["fibonacci"])
print('Cantidad de divisores: ',len(list(data["divisores"])))
print('Divisores: ',data["divisores"])
