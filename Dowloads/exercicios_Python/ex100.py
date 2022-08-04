from random import randint
def sorteio(num):
    print('Sorteando 5 valores da lista', end=' ')
    for c in range(0, 5):
        b = (randint(1, 10))
        num.append(b)
        print(f'{b}', end=' ')


def somapar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'\nSomando os valores de {num} temos {soma}')



numeros = []
sorteio(numeros)
somapar(numeros)

