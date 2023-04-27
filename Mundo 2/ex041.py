# Definir idade de atleta e sua categoria de competição
from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print(f'O atleta tem {idade} anos!')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')