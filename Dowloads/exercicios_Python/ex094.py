dicio = {}
lista = []
resp = ''
soma = 0
while True:
    dicio['nome'] = str(input('Nome: '))
    while True:
        dicio['sexo'] = str(input('sexo: ')).upper()[0]
        if dicio['sexo'] in 'MF':
            break
        print('Erro! digite apenas M ou F')
    dicio['idade'] = int(input('idade: '))
    soma += dicio['idade']
    lista.append(dicio.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro responda so S ou N')
    if resp == 'N':
        break
print('-=' * 30)
media = soma / len(lista)
print(f' A) Ao todo temos {len(lista)} pessoas cadastradas ')
print(f' B) A media de idade é de {media:.2f} anos ')
for p in lista:
     if p['sexo'] == 'F':
         print(f' C) As mulheres cadastradas foram: {p["nome"]}')
for p in lista:
    if p['idade'] >= media:
        print(' D) As pessoas acima da media são: ', end='')
        print('        ')
        for k, v in p.items():
            print(f' {k} = {v} ', end='')
