from datetime import date
ano = int(input('Digite o ano para análise! Digite 0 para verificar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano} Não é Bissexto')
