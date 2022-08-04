somaid = maior = menos20 = 0
maisv = ''
for c in range(1, 5):
    print(f'==== {c}ªPessoa ====')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    somaid += idade
    sexo = str(input('Sexo:[M/F] ')).upper().strip()[0]
    if c == 1 and sexo == 'M':
        maior = idade
        maisv = nome
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            maisv = nome
    if idade < 20 and sexo == 'F':
        menos20 += 1
media = somaid / 4
print(f'A media de idade do grupo é {media:.1f} anos')
print(f'O homem mais velho tem {maior} idade e se chama {maisv}.')
print(f'Ao todo são {menos20} com menos de 20 anos.')
