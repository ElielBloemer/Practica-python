# Escreva um programa que pergunte o salário  de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule
# um aumento de 10 %. Para inferiores ou iguais o aumento é de 15 %.
salario = float(input(' Digite o salário :'))
if salario <= 1250.00:
    print('O salario de {:.2f}, 15% = {:.2f}, total {:.2f} + {:.2f} = {:.2f}'.format(salario,salario * 0.15,salario,salario * 0.15 ,(salario * 0.15) + salario))
else:
    print('O salario de {:.2f}, 10% = {:.2f}, total {:.2f} + {:.2f} = {:.2f} '.format(salario,salario*0.1, salario,salario * 0.1, salario + (salario * 0.1)))


