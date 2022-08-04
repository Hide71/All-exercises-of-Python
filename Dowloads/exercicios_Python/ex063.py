print('_'*30)
print('Sequência de Fibonacci'.center(30))
print('_'* 30)
termo = int(input('Quantos termos você quer mostrar? '))
c = 2
n1 = 0
n2 = 1
print(n1, n2, end='-> ')
while c < termo:
    n3 = n1 + n2
    c += 1
    print(f'{n3}', end='-> ')
    n1 = n2
    n2 = n3
print('FIM')



