lista = []
nota = []
total = []
while True:
    lista.append(str(input('nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    m = (nota[0] + nota[1]) / 2
    lista.append(nota[:])
    nota.clear()
    lista.append(m)
    total.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"nº"} {"nome":>5} {"media":>15}')
print('_'*60)
for i, v in enumerate(total):
    print(f'{i} {v[0]:>5}  {v[2]:>15}')
while True:
    n = int(input('Mostrar nota de qual aluno?(999 para parar): '))
    if n == 999:
        break
    else:
        if n <= len(total) - 1:
            print(f"As notas de {total[n][0]} são {total[n][1]}")
        else:
            print('Erro digite novamente!')