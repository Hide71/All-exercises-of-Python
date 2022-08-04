from datetime import date
atual = date.today().year
ano = int(input('Que ano quer analisar? 0 para ano atual: '))
if ano == 0:
    ano = atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')

