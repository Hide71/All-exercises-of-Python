dist = int(input('\33[7:40mA distância em metros: \33[m'))
print(f'\33[7:40mA medida {dist:.1f}m corresponde a:\33[m ')
print(f'\33[7:43m{dist / 1000} KM \33[m\n\33[7:43m{dist / 100} HM \33[m\n\33[7:43m{dist / 10} DAM\33[m \n\33[7:41m{dist * 10} DM\33[m \n\33[7:41m{dist * 100} CM\33[m \n\33[7:41m{dist * 1000} MM\33[m')