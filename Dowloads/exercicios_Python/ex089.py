lista = []
while True:
     nome = str(input('Nome: '))
     n1 = float(input('Nota1: '))
     n2 = float(input('Nota2: '))
     media = (n1 + n2) / 2
     lista.append([nome, [n1, n2], media])
     resp = str(input('Quer continuar?[S/N]: '))
     if resp in 'Nn':
          break
print('=' *30)
print('No.   Nome           media')
print('-' *30)
for i, v in enumerate(lista):
     print(f'{i}: {v[0]:>7}  {v[2]:>15}')
print('='* 30)
while True:
    i = int(input('Quer mostrar a nota de qual aluno?(999 para): '))
    if i == 999:
         print('Finalizado!!')
         break
    if i <= len(lista):
        print(lista[i][0], lista[i][1])
