# Ler 6 números inteiros e somar apenas os pares
soma = 0
quant = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número:'))
    if n % 2 == 0:
        soma += n
        quant += 1

print(f'A soma do(s) {quant} número(s) pares é = {soma}')
