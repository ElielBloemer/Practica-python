nome = 'Eliel Bloemer Correa'
print('MUITO PRAZER EM TE CONHECER, {}{}{}!!!!'.format('\033[31m',nome,'\033[m'))# cores no python
a = float(input('\033[1;31;46m INGRESE EL PRIMER VALOR'))
b = float(input('INGRESE EL SEGUNDO VALOR'))
c = float(input('INGRESE EL TERCER VALOR'))
print('-='*20)
if a<b+c and b<a+c and c<a+b:
    print('O TRIANGULO É ')
    if a==b and b==c:
     print('TIPO EQUILATERO.')
    elif a!=b!=c!=a:
     print('TIPO ESCALENO.')
    else:
     print('TIPO ISÓCELES')
else :
   print('NAO É TRIANGULO')
