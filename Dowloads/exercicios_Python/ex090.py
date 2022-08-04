lista = dict()
lista['nome'] = str(input('Nome:'))
lista['media'] = float(input(f'media de {lista["nome"]}: '))
if lista['media'] >= 7:
    lista['situação'] = 'aprovado'
elif 5.1 <= lista['media'] <= 6.9 and lista['media'] :
     lista['situação']= 'recuperação'
else:
    if lista['media'] <= 5.0:
       lista['situação'] = 'reprovado'
for k, v in lista.items():
    print(f'{k} é igual a {v}')