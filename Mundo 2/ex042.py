#Ler segmentos e dizer se formam algum tipo de triângulo
s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os lados podem formar um triângulo', end=' ')
    if s1 == s2 == s3:
        print('Equilátero')
    elif s1 != s2 != s3 != s1:
        print('Escaleno')
    else:
        print('Isósceles')
        
else:
    print('Os lados NÃO podem formar um triângulo!')