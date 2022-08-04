from datetime import datetime
from time import sleep
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
if trabalhador['ctps'] == 0:
    for k, v in trabalhador.items():
         print(f'-{k} tem o valor {v}')
         sleep(1)
else:
    trabalhador['contratação'] = int(input('Ano de contratação?: '))
    trabalhador['salario'] = float(input('Salario?:R$ '))
    trabalhador['aposentadoria'] =  trabalhador['contratação'] + 35 - nasc
    for k, v in trabalhador.items():
         print(f'-{k} tem o valor {v}')
         sleep(1)
