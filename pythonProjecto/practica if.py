# Escreva um programa que pergunte o salário  de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule
# um aumento de 10 %. Para inferiores ou iguais o aumento é de 15 %.
salario = float(input("DIGITE UM SALARIO"))
if salario > 1.250 :
    print(' SEU SALARIO É : {:.2f} E COM AUMENTO DE 10 % É {:.2f}'.format(salario, salario+(salario*0.1)))
else:
    print(' SEU SALARIO É : {:.2f}  E COM AUMENTO DE 15% SERIA : {:.2f}'.format(salario,salario + (salario*0.15)))
    print(' GRACIAS!')