from datetime import date
def voto(anon):
    atual = date.today().year
    idade = atual - anon
    if idade <= 15:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 < idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL '



print('-='*30)
nasc = int(input('Em que ano voce nasceu?: '))
print(voto(nasc))