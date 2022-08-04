valor = float(input('Valor da casa:R$  '))
sal = float(input('salário do comprador:R$  '))
fin = int(input('Quantos anos de financiamento: '))
max = (sal *30) /100
prest = fin * 12
preço = valor / prest
print(f'Para pagar uma casa de R${valor:.2f}em {fin} anos a prestação será de R${preço:.2f} abaixo de 30% que é R${max:.2f}, Portanto')
if preço <= max:
    print('\33[32mEMPRESTIMO APROVADO!!')
else:
    print('\33[32mEMPRESTIMO NEGADO!!')