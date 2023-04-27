# Programa para Calcular empréstimo para casa
casa = float(input('Digite o valor da Casa: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite a quantidade de anos que deseja pagar:'))
prestacao = casa / (anos * 12)

if prestacao > sal * 0.30:
    print('Infelizmente seu empréstimo não pode ser aprovado nesse contexto!')
elif prestacao <= sal * 0.30:
    print(f'Seu empréstimo pode ser aprovado com a prestação mensal de R${prestacao:.2f} por {anos} anos!')
    