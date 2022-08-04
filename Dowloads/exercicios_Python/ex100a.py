from random import randint
from time import sleep
def sorteia(lista):
    for c in range(0, 5):
        n = (randint(0, 10))
        lista.append(n)
    print(f'Sorteando {len(lista)} valores da lista' , end=' ')
    for i, v in enumerate(lista):
        sleep(.3)
        print(f'{v}', end=' ')
    print('Pronto!')

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')



numeros = []
sorteia(numeros)
somapar(numeros)




