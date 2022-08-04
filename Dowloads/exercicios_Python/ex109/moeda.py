
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