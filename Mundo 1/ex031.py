v = float(input('Digite a distância de sua viagem: KM '))
if v > 200:
    print(f'Viagem de {v} Km. A tarifa será de R$0,45 por Km!')
    preco = v * 0.45
else:
    preco = v * 0.50
    print(f'Viagem de {v} Km. A tarifa será de R$0,50 por Km!')
print(f'O preço da sua passagem é de R${preco:.2f}')
