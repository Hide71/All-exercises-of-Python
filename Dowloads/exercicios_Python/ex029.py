velo = int(input('Qual a velocidade atual do carro?: '))
multa = (velo - 80) * 7
if velo > 80:
    print('\33[34mMultado! você excedeu o limite de 80 km/h')
    print(f'Sua multa sera de \33[37mR$ {multa:.2f} ')
print('\33[36mTenha um bom Dia! Dirija com segurança!')