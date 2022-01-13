'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado
 e mostre quantas vezes aparece a letra “A”, em que posição ela aparece
 a primeira vez e em que posição ela aparece a última vez.'''
frase = (str(input(' Digite uma frase :')).strip()).lower()
print(' a quantidade de caracteres A é {}'.format(frase.count('a')))
print(' a primera letra A na frase esta na posicão {}'.format(frase.find('a')+1)) #busca a letra do começo para frente
print(' a ultima letra A esta na posição {}'.format(frase.rfind('a')+1))# rfind busca a letra vindo de tras para frente
