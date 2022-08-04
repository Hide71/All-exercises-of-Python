print('=' * 30)
print(' 10 TERMOS DE UMA PA'.center(30))
print('=' * 30)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
for c in range(pt, pt + (10 * rz), rz):
    print(f'{c} ', end='-> ')
print('ACABOU!!!')