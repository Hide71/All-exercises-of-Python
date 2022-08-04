preço = float(input('\33[37mQual é o preço do produto?:R$ '))
print(f'\33[35mO produto que custava R${preço}, com desconto de 5% vai custar R$ {preço - (preço * 5 / 100):.2f}.')