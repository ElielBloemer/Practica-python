# Desenvolva um programa que pergunte a distância de uma viagem em Km,
# Calcule o preço da passagem, cobrando R$ 0,50 por KM, para viagem
# até 200 km e R$ 0,45 para viagens mais longas.
km = int(input(' Digite a quantidade de quilomêtros da viagem :'))
if km <= 200:
    print(' o valor da passagem à pagar pelos {} KM seria {:.2f}'.format(km, km * 0.50))
else:
    print(' o valor da passagem à pagar pelos {} KM seria {:.2f}'.format(km, km * 0.45))
print(' obrigado !')
