resp = 'Ss'
c = soma =  maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    if c == 0:
        maior = n
        menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    c += 1
    soma += n
    resp = str(input('Quer continuar?[S/N]: '))
print(f'Você digitou {c} numeros, e a media foi {soma / c:.2f}')
print(f'O maior valor foi {maior}, e o menor foi {menor}')





