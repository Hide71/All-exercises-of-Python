sal = float(input('Qual é o salário do funcionário?: '))
if sal <= 1250:
    nsal = sal + (sal * 15) / 100
    print(f"Seu novo salario será de R${nsal:.2f}")
else:
    nsal = sal + (sal * 10) / 100
    print(f'Seu novo salario será de R${nsal:.2f}')