from math import pow, sqrt, hypot
cato = float(input('Digite o valor do cateto oposto:'))
catadj = float(input('Digite o valor do cateto adjacente:'))

print(f'O valor da hipotenusa é = {sqrt(pow(cato,2)+pow(catadj, 2)):.3f}')

'''print(f'O valor da hipotenusa é = {sqrt((cato*cato)+(catadj*catadj)):.3f}')

print(f'O valor da hipotenusa é = {sqrt((cato**2)+(catadj**2)):.3f}')

print(f'O valor da hipotenusa é = {((cato**2)+(catadj**2))**(1/2):.3f}')'''

print(f'O valor da hipotenusa é = {hypot(cato, catadj):.3f}')
