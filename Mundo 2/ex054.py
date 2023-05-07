# Verificar número de maiores de menores de idade pela data de nascimento
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if atual - nasc < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoas atingiram a maioridade e {menor} ainda não atingiram a maioridade')
