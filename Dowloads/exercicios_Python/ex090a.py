dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Media: '))
if dic['media'] <= 5:
    dic['situação'] = 'Reprovado'
elif dic['media'] <= 7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Aprovado'
for k, i in enumerate(dic):
    print(f'-> {i} é igual a {dic[i]}')