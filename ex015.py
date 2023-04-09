qkm = float(input('Digite a quantidade de Kilômetros percorridos pelo veículo:'))
qdias = int(input('Digite a quantidade de dias alugados:'))

print('Preço do carro por dia: R$60,00 \nPreço por Km percorrido: R$0,15')
print(f'O preço a ser pago é = R${(qkm * 0.15) + (qdias * 60):.2f}')
