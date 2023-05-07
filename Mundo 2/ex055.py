# Verificar o peso de 6 pessoas e dizer o maior e o menor
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª Pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior Peso digitado foi: {maior}KG')
print(f'O menor Peso digitado foi: {menor}KG')
