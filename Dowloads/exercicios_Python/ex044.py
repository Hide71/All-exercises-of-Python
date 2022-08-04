print('\33[30m=\33[m' *30)
print('\33[30mLOJAS UNIVESP\33[m'.center(30))
print('=\33[30m' * 30)
preço = float(input('\33[35mPreço das compras:R$ \33[m'))
print('''\33[33mFORMAS DE PAGAMENTO
[1] à vista dinheiro / cheque
[2] á vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão\33[m''')
opção = int(input('Qual é a opção?: '))
if opção == 1:
    valor = preço - (preço * 10 / 100)
    print(f'Sua compra á vista será R${valor:.2f} COM DESCONTO DE 10%')
elif opção == 2:
    valor = preço - (preço * 5 / 100)
    print(f'Sua compra à vista no cartão será R${valor:.2f} COM DESCONTO DE 5%')
elif opção == 3:
    parcelas = int(input('Quantas parcelas?: '))
    if parcelas <= 2:
        valor = preço
        parc = valor / parcelas
        print(f"sua compra em até 2x no cartão será R$ {parc:.2f} SEM JUROS.")
elif opção == 4:
    parcelas = int(input('Quantas parcelas?: '))
    if parcelas >= 3:
        valor = preço + (preço * 20 / 100)
        parc = valor / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parc:.2f} COM JUROS')
else:
    valor = 0
    print('OPÇÃO INVALIDA! Digite novamente')
print(f'Sua compra de \33[36mR${preço:.2f}\33[m, vai custar \33[31mR${valor:.2f}\33[m, no FINAL.')

