from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc}, em {atual}, tem {idade} anos.')
if idade <= 17:
    falta = 18 - idade
    print(f'Ainda faltam {falta} anos para o alistamento.\nSeu alistamento será em {atual + falta}')
else:
    falta = idade - 18
    print(f'Você já deveria ter se alistado em {falta} anos.\nSeu alistamento foi á  {atual - falta}')
