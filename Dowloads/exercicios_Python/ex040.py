n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Quem tirou nota {n1} e nota {n2} teve a media {media:.1f}')
if media < 5:
    print('Aluno Reprovado!!')
elif media <= 6.9:
    print('Aluno em Recuperação!!!')
else:
    print('Aluno Aprovado!!')

