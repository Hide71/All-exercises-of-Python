qq = str(input('\33[35:40mDigite algo: '))
print('\33[35mO tipo primitivo é :\33[m' , type(qq))
print('\33[35:40mSó tem espaços?\33[m ' ,(qq.isspace()))
print('\33[35:40mÉ um numero?\33[m', (qq.isnumeric()))
print('\33[35:40mÉ alfabetico?\33[m ', (qq.isalpha()))
print('\33[35:40mEstá em maiúsculas?\33[m', (qq.isupper()))
