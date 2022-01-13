print('{:=^40}'.format(' LOJAS ELIEL '))
valor = float(input('Digite o valor das compras $ :'))
print(('''FORMA DE PAGAMENTO
[1] - Á vista dinheiro/cheque
[2] - á vista cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão'''))
opcao = int(input('Qual é a opção de pagamento?'))
if opcao==1:
    print(' O valor da compra é {:.2f} com desconto de 10 % ficaria {:.2f} '.format(valor,valor-(valor*0.10)))
elif opcao==2:
    print(' O valor da compra é {:.2f} com desconto de 5 % ficaria {:.2f} '.format(valor,valor-(valor*0.5)))
elif opcao==3:
    print(''' O valor da compra é {:.2f} 
    2 x parcelas de {:.2f} '''.format(valor,valor/2))
elif opcao==4:
    parcelas = int(input(' Em quantas parcelas?'))
    print('''O valor da compra é {:.2f} com parcelas de {} x de R$ {:.2f}
    Valor total da compra seria de R$ {:.2f}'''.format(valor,parcelas,(valor+(valor*0.20))/parcelas,valor+(valor*0.20)))
else:
    print(' OPÇÃO INCORRETA! ')