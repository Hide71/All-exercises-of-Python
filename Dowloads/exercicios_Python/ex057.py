sexo = ''
while True:
    sexo = str(input('Informe seu sexo: ')).upper().strip()[0]
    if sexo in 'MF':
        break
    print('ERRO! Informe um sexo valido!')
print(f'Sexo {sexo} registrado com sucesso! ')


