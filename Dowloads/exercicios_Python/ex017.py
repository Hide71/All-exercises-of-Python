from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
print(f'A Hipotenusa vai medir: {hypot(co, ca):.2f}')
