from datetime import date
atual = date.today().year
contn = contv = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}º pessoa nasceu?: '))
    idade = atual - nasc
    if idade < 18:
        contn += 1
    else:
        contv += 1
print(f'Ao todo temos {contn} pessoas menores de idade.\nTemos também {contv} pessoas maiores de idade')
