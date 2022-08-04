print('='*30)
print('Lojas Univesp'.center(30))
print('='*30)
totp = maisc = maisb = c = 0
nom = nome = ""
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preco R$: '))
    if preço > 1000:
        c += 1
    if totp == 0:
        maisc = preço
        nom = prod
        maisb = preço
        nome = prod
    else:
        if preço > maisc:
            maisc = preço
            nom = prod
        if preço < maisb:
            maisb = preço
            nome = prod
    totp += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]:')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total de compras foi: R${totp:.2f}.')
print(f'O produto mais caro foi {nom} custando R${maisc:.2f} ')
print(f'O produto mais barato  foi {nome} custando R${maisb:.2f}.')
print(f'Temos {c} produtos custando acima de R$ 1000,00')