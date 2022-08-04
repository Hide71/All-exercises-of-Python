n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n +1):
    if n % c == 0:
        tot += 1
        print(f'\33[33m{c}\33[m', end=' ')
    else:
        print(f'{c}', end=' ')
if tot == 2:
    print(f'\nO numero {n} é divisivel {tot} vezes, portanto é  PRIMO')
else:
    print(f'\nO numero {n} é divisivel {tot} vezes, portanto não é PRIMO')