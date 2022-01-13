#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5 % de desconto.
n = float(input(' Digite o preço do produto :'))
print('O valor desse produto é {} e com 5% de desconto {:.2f}'.format(n,n-(n*0.05)))
