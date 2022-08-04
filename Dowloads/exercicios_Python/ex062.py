print('\33[33m=\33[m' *30)
print('\33[36mGerador de P.A.\33[m'.center(30))
print('\33[33m=\33[m' * 30)
pt = int(input('\33[32mDigite o primeiro termo:\33[m '))
rz = int(input('Digite a razão: '))
c = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while c < total:
        print(pt, end='->')
        pt += rz
        c += 1
    print(' Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print(f'Progressão terminada com {total} termos mostrados')
