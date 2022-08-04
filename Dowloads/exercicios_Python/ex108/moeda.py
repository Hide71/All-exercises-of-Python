
def aumentar(p=0, q=0):
    t = p + (p * q / 100)
    return t

def diminuir(p=0, q=0):
    t = p - (p * q / 100)
    return t

def dobro(p=0):
    t = p * 2
    return t
def metade(p=0):
    t = p / 2
    return t

def moeda(p, b ='R$'):
    return (f'{b} {p:.2f}'.replace('.', ','))