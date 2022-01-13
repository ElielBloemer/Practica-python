'''exercício 36
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder o 30 % do salário,ou então o empréstimo será negado.
'''
valorCasa = float(input('QUAL É O VALOR DA CASA ? '))
salario = float(input(' DIGITE O SALARIO '))
anos = int(input('QUANTOS ANOS VOÇÊ VAI PAGAR A CASA? '))
meses = int(anos*12)
prestacao = float(valorCasa/(meses))

limite = float(salario*0.30)
if prestacao>limite:
    print('Infelizmente as prestaçoes superam 30% do seu salario')
    print(' Valor da casa $ {:.2f}, salario $ {:.2f} '.format(valorCasa, salario, anos, meses))
    print(' 30 % de {} é {}'.format(salario,limite))
    print(' Emprestimo negado.')
else :
    print('Parabens! seu emprestimo foi autorizado.')
    print(' Valor da casa $ {:.2f}, salario $ {:.2f} '.format(valorCasa, salario, anos, meses))
    print(' A casa será paga em {} anos, serão pagas {} prestações de  $ {:.2f}'.format(anos, meses, prestacao))



