l = float(input('Largura da parede: '))
a = float(input('\33[33mAltura da parede: '))
area = l * a
tinta = area / 2
print(f'\33[34mSua parede tem a dimensão de {l} x {a} e sua area é de {area}M2.')
print(f'Para pintar essa parede você vai precisara de {tinta} litros de tinta.')