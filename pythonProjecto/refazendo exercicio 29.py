#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input(' DIGITE OS KILOMETROS DO CARRO :'))
if vel >= 80 :
    print('VOCE EXCEDEU O LIMITE DE VELOCIDADE!')
    print('O VALOR A SER A PAGO É : {:.2f}'.format(vel*7))
else:
    print(' VOCE NAO PASSOU O LIMITE DE VELOCIDADE ')
    print(' OBRIGADO !')