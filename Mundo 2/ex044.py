# Simulador de gerência de uma loja
prod = float(input('Digite o valor gasto em produtos: R$'))
op = int(input('''FORMAS DE PAGAMENTO
[1] à Vista/cheque
[2] à Vista/ Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão
Qual a opção desejada? '''))

if op == 1:
    desc = prod - (prod * 0.10)
    print(f'O produto custará R${desc:.2f} com desconto')

elif op == 2:
    desc = prod - (prod * 0.05)
    print(f'O produto custará R${desc:.2f} com desconto')

elif op == 3:
    print(f'A compra será parcelada de 2x de R${prod / 2:.2f}')
    print(f'A compra de R${prod} irá custar R${prod:.2f} sem juros')

elif op == 4:
    parc = int(input('Quantas parcelas?'))
    juros = prod * 0.20
    print(f'A compra será parcelada de {parc}x de R${(prod + juros) / parc:.2f}')
    print(f'A compra de R${prod} irá custar R${prod + juros:.2f} no final com juros')
else:
    print('Opção Inválida de pagamento! Tente novamente')
print('Fim do programa!!!')