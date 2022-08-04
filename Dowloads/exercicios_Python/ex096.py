def area(a, b):
    p = a * b
    return f'A area do terreno {a} x {b} é de {p}m2'

print('  Controle de terrenos   ')
print('-' * 30)
lar = float(input('largura(m):  '))
comp = float(input('comprimento(m): '))
print(area(lar, comp))
