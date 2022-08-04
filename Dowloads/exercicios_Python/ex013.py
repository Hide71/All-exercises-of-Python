sal = float(input('\33[40mQual é o salário do funcionário? : R$\33[m'))
print(f'\33[42mUm funcionário que ganhava {sal}, com o aumento de 15% passa a receber R$ {sal + (sal * 15 / 100):.2f}\33[m')
