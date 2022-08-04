lista = []
maior = menor = 0
for c in range(0, 5):
    n = int(input(f'Digite o valor para a posição {c}: '))
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    lista.append(n)
print('-'*30)
print(f'Voce digitou os valores: {lista}')
print(f'O maior valor digitado foi: {maior} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi: {menor} nas posições: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')



