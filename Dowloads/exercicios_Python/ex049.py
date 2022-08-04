n = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1, 11):
    print(f'\33[33m{n} x {c:2} = {(n * c)}')