from random import randint
lista = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print('Os numeros gerados foram: ', end='')
for n in lista:
    print(f'{n}', end=' ')
print(f'\nO maior valor gerado foi: {max(lista)}')
print(f' menor valor gerado foi: {min(lista)}')


