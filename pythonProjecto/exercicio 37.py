num = int(input('Digite um numero inteiro :'))
print('''Escolha a base de conversão:
[1] - BINARIO 
[2] - OCTAL 
[3] - HEXADECIMAL ''')
opcao = int(input(" Digite a opção : "))
if opcao==1:
    print('O NUMERO {} CONVERTIDO PARA BINARIO É {}. '.format(num,bin(num)[2:]))
elif opcao==2:
   print(' O NUMERO {} CONVERTIDO PARA OCTAL É {}. '.format(num,oct(num)[2:]))
elif opcao==3:
   print(' O NUMERO {} CONVERTIDO PARA HEXADECIMAL É {}. '.format(num,hex(num)[2:]))
else :
 print('OPCAO INVALIDA!')