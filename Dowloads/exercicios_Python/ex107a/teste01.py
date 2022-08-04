from ex107a import moeda01
valor = float(input('Digite o preço: R$ '))
print(f'O dobro de R$ {valor:.2f} é R$ {moeda01.dobro(valor)}')
print(f'A metade de R$ {valor} é R$ {moeda01.metade(valor)}')
print(f'Aumentando 10% temos R$ {moeda01.aumentar(valor, 10)} ')
print(f'Diminuindo 5% temos R$ {moeda01.diminuir(valor, 5)}')