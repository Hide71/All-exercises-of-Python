def area(a, b):
    area = a * b
    print(f'A area de {a}x {b} é de {area}m2')



print('\33[33mControle de terrenos')
print('-='*30)
l = float(input('Largura: '))
c = float(input('Comprimento:'))
area(l, c)
