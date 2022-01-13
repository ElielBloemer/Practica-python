#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
nome1 = input(' digite o primero nome :')
nome2 = input(' digite o segundo nome :')
nome3 = input(' digite o tercero nome :')
nome4 = input(' digite o quarto nome :')
lista = [nome1,nome2,nome3,nome4]
print(' o alumno(a) escolhido é {}'.format((random.choice(lista))))
