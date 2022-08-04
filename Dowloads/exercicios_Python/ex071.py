print('='*30)
print('BANCO UNIVESP S/A'.center(30))
print('+'*30)
valor = float(input('Que valor você quer sacar?: '))
ced = 50
nvalor = valor
totced = 0
while True:
    if nvalor >= ced:
       nvalor -= ced
       totced += 1
    else:
        if totced > 0:
           print(f'Total de {totced} cedulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if nvalor == 0:
            break
