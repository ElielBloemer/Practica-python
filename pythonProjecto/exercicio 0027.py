'''faça um programa que leia, o nome de uma pessoa, depois mostrar o primeiro e o ultimo nome,  separadamente.
exemplo : Ana Maria de Souza
primeiro: Ana.
último: Souza.'''
nome = str(input('Digte um nome : ')).split()
print('o primeiro nome é {}'.format(nome[0]))
print('o ultimo nome é {}'.format(nome[len(nome)-1]))#uso o len para calcular o tamanho total da lista e resto uma posiçao
#mostrando assim a ultima.