n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# CASO N1 SEJA MAIOR
if n1 > n2 and n1 > n3:
    print(f'{n1:.0f} é o maior número')
    if n2 < n3:
        print(f'{n2:.0f} é o menor número')
    else:
        print(f'{n3:.0f} é o menor número')
# CASO N2 SEJA MAIOR
if n2 > n1 and n2 > n3:
    print(f'{n2:.0f} é o maior número')
    if n1 < n3:
        print(f'{n1:.0f} é o menor número')
    else:
        print(f'{n3:.0f} é o menor número')

# CASO N3 SEJA MAIOR

if n3 > n1 and n3 > n2:
    print(f'{n3:.0f} é o maior número')
    if n2 < n1:
        print(f'{n2:.0f} é o menor número')
    else:
        print(f'{n1:.0f} é o menor número')