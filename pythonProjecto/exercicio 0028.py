# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 a 5 e peça para o usuário  tentar descobrir qual foi o
# número escolhido pelo computador.  O programa deverá escrever
# na tela se o usuário ganhou o perdeu.
import random
print('O computador já escolheu um numero!')
num1 = random.randint(0, 5)  # função random.randint(0,5) me gera numeros de 0 a 5 aletoriamente
print('tente adivinhar qual numero é !')
num = int(input(' digite o numero '))
if num == num1:
    print(' parabéns voce adivinhou o numero!  :)')
    print(' o computador escolheu o numero {} '.format(num1))
else:
    print(' voce falhou! o computador ganhou :(')
    print(' o computador escolheu o numero {} '.format(num1))
print('fim')
