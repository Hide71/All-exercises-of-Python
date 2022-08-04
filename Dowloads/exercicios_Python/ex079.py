lista = []
resp = 's'
while resp != 'n':
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
         print('Valor duplicado!! Não vou adicionar')
    resp = str(input('Quer continuar?[S/N]: '))
print('-='*30)
lista.sort()
print(f'voce digitou os valores {lista}')

