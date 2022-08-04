from datetime import datetime
def voto(a):
    atual = datetime.now().year
    idade = atual - a
    if idade <= 15:
        return f'Com {idade} anos: NÃO VOTA!'
    elif idade == 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'



nasc = int(input('Em que ano voce nasceu?: '))
r1 = (voto(nasc))
print(r1)
