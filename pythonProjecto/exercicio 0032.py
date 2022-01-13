#Faça um programa que leia um ano e mostre se ele é BISSEXTO.
ano = int(input('Digite o ano para saber se é bissexto :'))
if (ano%4)==0 and (ano%100)!=0 :
    print('{} é um ano bissexto'.format(ano))
elif (ano%400)==0 :
    print('{} é um ano bissexto'.format(ano))
else :
    print('{} não é um ano bissexto'.format(ano))



