#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = input(' digite o primero nome :')
n2 = input(' digite o segundo nome :')
n3 = input(' digite o terceiro nome :')
n4 = input(' digite o quarto nome :')
lista = [n1,n2,n3,n4]
shuffle(lista)
print(' a ordem de apresentação é')
print(lista)
