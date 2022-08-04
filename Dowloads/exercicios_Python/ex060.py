n = int(input('Digite um núero para calcular o seu fatorial: '))
c = n
f = 1
print(f'Calculando o {n}!:')
while c > 0:
    print(f'{c}', end=' ')
    f *= c
    c -= 1
    print('x' if c >=1  else '=', end=' ')
print(f'{f}', end=' ')



