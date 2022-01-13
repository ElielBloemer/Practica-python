'''Exercício Python 17: Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o
comprimento da hipotenusa.'''
'''co = float(input(' comprimento do cateto oposto :'))
ca = float(input(' cateto adjacente : '))
h = (co**2 + ca**2)**(1/2)
print(' a hipotenusa vai medir {:.2f}'.format(h))'''
import math
co = float(input(' comprimento do cateto oposto :'))
ca = float(input(' cateto adjacente : '))
hi = math.hypot(co,ca)
print('  HIPOTENUSA MEDE {:.2f}'.format(hi))

