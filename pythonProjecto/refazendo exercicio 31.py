#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 para viagens mais longas.
#dis = float(input("DIGITE QUANTOS KM DESEJA VIAJAR ?"))
#if dis >= 200:
 #   print(" {:.2f} KM CORRESPONDE A : {:.2f}".format(dis,dis*0.50))
  #  print('OBRIGADO!')
#else:
 #   print(" {:.2f} KM CORRESPONDE A : {:.2f}".format(dis,dis*0.45))
  #  print('OBRIGADO!')
'''ano = int(input('DIGITE UM ANO '))
if (ano%4)==0 and (ano%100)!=0:
    print('O ANO {} É UM ANO BISSEXTO'.format(ano))
elif(ano%400)==0:
    print('O ANO {} É UM ANO BISSEXTO'.format(ano))
else:
    print("O ANO {} NÃO É BISSEXTO".format(ano))'''
num1 = int(input('DIGITE O NUMERO 1 :'))
num2 = int(input("DIGITE O NUMERO 2 :"))
num3 = int(input('DIGITE O NUMERO 3 :'))
if num1>num3 and num1>num2:
    if num2>num3:
        print('NUMEROS ORDENADOS \n NUM1 = {} \n NUM2 = {} \n NUM3 = {}'.format(num1,num2,num3))
    else:
        print('NUMEROS ORDENADOS \n NUM1 = {} \n NUM3 = {} \n NUM2 = {}'.format(num1,num3,num2))
elif num2>num1 and num2>num3:
        if num1 > num3:
            print('NUMEROS ORDENADOS \n NUM2 = {} \n NUM1 = {} \n NUM3 = {}'.format(num2,num1,num3))
        else:
            print('NUMEROS ORDENADOS \n NUM2 = {} \n NUM3 = {} \n NUM1 = {}'.format(num2,num3,num1))
else:
        if num1>num2:
            print('NUMEROS ORDENADOS \n NUM3 = {} \n NUM1 = {} \n NUM2 = {}'.format(num3,num1,num2))
        else:
            print("NUMEROS ORDENADOS \n NUM3 = {} \n NUM2 = {} \n NUM3 = {}".format(num3,num2,num1))

