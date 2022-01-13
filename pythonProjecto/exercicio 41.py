'''Exercício Python 041: A Confederação Nacional de Natação
precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''
anoNascimento = int(input('Digite o ano de nascimento do atleta:'))
import  math
idade = int(math.fabs(2021-anoNascimento))
if idade <=9:
    print(''' Atleta : MIRIM
       O atleta tem {} ano(s)'''.format(idade))
elif idade>9 and idade<=14:
    print(''' Atleta : INFANTIL 
    O atleta tem {} ano(s)'''.format(idade))
elif idade>14 and idade<=19:
    print('''Atleta : JÚNIOR
    O atleta tem {} ano(s)'''.format(idade))
elif idade>19 and idade<=25:
    print('''Atleta : SÊNIOR
    O atleta tem {} ano(s)'''.format(idade))
else :
    print('''Atleta : MASTER
    O atleta tem {} ano(s)'''.format(idade))