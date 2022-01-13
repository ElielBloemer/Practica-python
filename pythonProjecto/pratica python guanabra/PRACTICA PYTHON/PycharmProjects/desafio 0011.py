# faça um programa que leia a largura e a altura de uma parede em metros.
# calcule a sua area e a quantidade de tinta, necesaria para pinta-la.
# Sabendo que cada cada litro de tinta pinta uma area de 2 m quadrados
l = float(input('Digite a largura da parede :'))
a = float(input('Digite a altura da parede : '))
areaTotal = l * a
print('A área da parede é {}'.format(l*a))
print('Voce ira precisar de {} litros de tinta para pintar essa parede de {} metros quadrados. '.format(int((areaTotal/2)),areaTotal))
