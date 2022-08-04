lista = []
c = 0
while True:
    resp = ' '
    lista.append(int(input('Digite um numero: ')))
    c += 1
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print(f'Você digitou {c} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O numero 5 faz parte da lista')
else:
     print('Não foi adicionado o numero 5 na lista')

