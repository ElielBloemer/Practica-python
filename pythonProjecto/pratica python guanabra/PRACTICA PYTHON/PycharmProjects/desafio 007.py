# desenvolva um programa que leia as duas notas de um alumno, calcule e mostre a sua media
nome = input(' digite o nome do aluno :')
n = float(input(' digite a nota de matematica do primeiro semestre:'))
n1 = float(input(' digite a nota de matematica do segundo semestre :'))
print(' o aluno {}\n tirou no primeiro semestre em matematica a nota {} \n e no segundo semestre tirou a nota {}'.format(nome,n,n1), end= ' ')
print('o promedio da nota é {}'.format((n+n1)/2))
