#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um
#carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Digite a quantidade de dias que voce alugou o carro : '))
km = float(input(' Digite a quantidade de kilometros que voce andou com o carro :'))
print('Voce devera pagar R$ {:.2f} pelos {} dias usando o carro, e R$ {:.2f} pelos {:.0f} km corridos.'.format(dias*60,dias,km*0.15,km))
print(' O valor total seria R$ {:.2f}'.format(dias*60+km*0.15))
