
c = soma = 0
n = int(input('\33[34mDigite um número[999 para parar]: '))
while n != 999:
    soma += n
    c +=1
    n = int(input('Digite um número[999 para parar]: '))
print(f'\33[35mVocê digitou {c} números e a soma entre eles foi {soma}')


