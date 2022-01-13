#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar .
#US$ 1 = $ 140 .
n = float(input(' Digite a quantidade de dinheiro que voce tem na carteira :'))
print('Com {:.0f} pesos, voce poderá comprar US$ {:.2f}'.format(n,n/140))
