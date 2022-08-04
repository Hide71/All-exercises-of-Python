lista = ((int(input('Digite um numero: '))), (int(input('Digite outro numero: '))),
         (int(input('Digite mais um  numero: '))), (int(input('Digite o ultimo  numero: '))))
print(f'\33[33mVoce digitou os valores {lista}\33[m')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 not in lista:
    print('O valor 3 não apareceu na lista')
else:
     print(f'O valor 3 apareceu na {lista.index(3) + 1}º posição')
print(f'Os valore pares digitados foram : ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
print('\nFIM')

