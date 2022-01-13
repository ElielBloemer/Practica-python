'''Escreva um programa que leia dos números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior.
- o segundo valor é maior.
- Não existe valor maior, são números iguais.
'''
num1 = int(input('DIGITE O PRIMERO NUMERO : '))
num2 = int(input('DIGITE O SEGUNDO NUMERO : '))
if num1 > num2:
    print('O NUMERO {} É MAIOR QUE O NUMERO {}'.format(num1,num2))
elif num2 > num1:
    print('O NUMERO {} É MAIOR QUE O NUMERO {}'.format(num2,num1))
elif num2==num1:
    print(' Os numeros são iguais! ')