'''Escreva um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade :
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de alistar.
- Se já passou do tempo de alistamento.
seu programa deverá mostrar o tempo que falta ou o tempo que já passou.
'''
ano = int(input(' Digite o ano do nascimento : '))
if(2021-ano)<18:
    print('Ainda não é tempo de se alistar, pois falta {} ano(s)'.format(((2021-ano)-18)*(-1)))
elif(2021-ano)==18:
    print('ATENÇÃO! Esse ano voçê deve se alistar.')
else:
    print('Infelizmente, voçê já passou o tempo de se alistar em {} ano(s)'.format((2021-ano)-18))

