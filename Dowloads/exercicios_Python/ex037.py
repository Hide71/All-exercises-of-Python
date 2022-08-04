n = int(input('Digite um numero qualquer: '))
print('~' * 30)
print('BASE de Conversão')
print('~' * 30)
print('1 para Binário')
print('2 para Octal')
print('3 para Hexadecimal')
print('~' * 30)
esc = int(input('Escolha uma das opções'))
if esc == 1:
    print(bin(n)[2:])
elif esc == 2:
    print(oct(n)[2:])
elif esc == 3:
    print(hex(n)[2:])
