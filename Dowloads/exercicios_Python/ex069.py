c = hom = men20 = 0
while True:
    print('-'*30)
    print('Cadastre uma pessoa'.center(30))
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
         sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade >= 18:
        c += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        men20 += 1
    print('='*30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {c}.\nAo todo temos {hom} homens cadastrados.\nE temos {men20} mulheres com menos de 20 anos de idade.')
