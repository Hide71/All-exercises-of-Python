dias = int(input('\33[7:41mQuantos dias alugado?: \33[m'))
km = float(input('\33[42mQuantos quilometros rodados?:\33[m '))
valor = dias * 60 + km * 0.15
print(f'\33[43mO total a pagar é de R$ {valor:.2f}\33[m')