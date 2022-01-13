#Escreva um programa que leia a velocidade de um carro,
# se ele ultrapassar 80km/h, mostre um mensagem dizendo
# que ele foi multado, a multa vai custar R$ 7,00 por
# cada quilômetro acima do limite.
km = int(input(' Digite a velocidade alcançada com o automóvel :'))
if km > 80 :
    print('O senhor passou do limite de kilometro !')
    print(' Devera pagar R$ {:.2f} devido ao exceso de velocidade'.format((km-80)*7))
else :
    print(' o senhor não passou do limite de velocidade ')
print(' obrigado !')

