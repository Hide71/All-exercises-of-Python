print('Gerador de P.A. : '.center(30))
print('=' * 30)
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
c = 0
while c < 10:
    c += 1
    print(f'{pt}', end='->')
    pt += rz
print(' FIM')

