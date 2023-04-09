sal = float(input('Digite o salário atual do funcionário: R$'))
if sal > 1250:
     print('Salário acima de R$1250,00. Sua comissão será de 10%!')
     sal = sal + sal * 0.10
else:
     print('Salário menor ou igual a R$1250,00. Sua comissão será de 15%!')
     sal = sal + sal * 0.15
print(f'Seu novo salário é = R${sal:.2f}')
