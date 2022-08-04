
def aumentar(p=0, q=0, form=False):
    t = p + (p * q / 100)
    return t if form is False else moeda(t)

def diminuir(p=0, q=0, form=False):
    t = p - (p * q / 100)
    return t if not form else moeda(t)

def dobro(p=0, form=False):
    t = p * 2
    return t if form is False else moeda(t)
def metade(p=0, form=False):
    t = p / 2
    return t if not form else moeda(t)

def moeda(p, b ='R$'):
    return (f'{b} {p:.2f}'.replace('.', ','))

def resumo(p=0, a=10, b=20):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado \t{moeda(p)} ')
    print(f'Dobro do preço \t\t{dobro(p, True)}')
    print(f'Metade do preço  \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a , True)}')
    print(f'{b}% de redução: \t{diminuir(p, b, True)}')