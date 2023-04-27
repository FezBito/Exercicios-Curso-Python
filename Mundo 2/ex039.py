# Calcular anos para alistamento Militar
from datetime import date
nasc = int(input('Digite o ano de seu nascimento: '))
atual = date.today().year #Pegar ano atual

idade = atual - (nasc)
print(f'Quem nasceu em {nasc} possui {idade} ano(s) em {atual}!')

if idade == 18:
    print('Você tem que se alistar ESSE ANO!')

elif idade < 18: 
    print(f'Ainda restam {18-idade} anos para você se alistar!')
    print(f'Seu alistamento será em {atual + (18-idade)}')

elif idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s)!')
    print(f'Seu alistamento foi em {atual + (18 - idade)}')