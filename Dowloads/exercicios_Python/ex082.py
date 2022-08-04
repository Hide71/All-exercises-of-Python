lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
         impar.append(n)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?:'))
    if resp in 'Nn':
        break
print(f'A lista completa é: {lista}')
print(f'A lista par é: {par}')
print(f'A lista impar é: {impar}')
