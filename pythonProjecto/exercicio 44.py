from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(''' ====== OPÇOES =======
[0] - Pedra 
[1] - PAPEL 
[2] - TESOURA
''')
jogador = int(input('Digite sua opcao: '))
print('-=' * 20)
print(' o computador escolheu {}'.format(itens[computador]))
if jogador >= 0 and jogador <= 2:
    print(' O jogador escolheu {}'.format(itens[jogador]))
    print('-=' * 20)
    if computador == 0:  # computador jogou pedra
        if jogador == 0:  # jogador jogou pedra
            print(' Empate entre voce e o computador. ')
        elif jogador == 1:  # jogador jogou papel
            print(' Parabéns Voce ganhou!')
        else:  # jogador jogou tesoura
            print('Infelizmente voce perdeu :( ')
    elif computador == 1:  # computador jogou papel
        if jogador == 0:  # jogador jogou pedra
            print(' Infelizmente voce perdeu :( ')
        elif jogador == 1:  # jogador jogou papel
            print('Empate entre voce e o computador.')
        else:  # jogador jogou tesoura
            print(' Parabéns Voce ganhou!')
    elif computador == 2:  # computador jogou tesoura
            if jogador == 0:  # jogador jogou pedra
                print('Parabéns Voce ganhou! ')
            elif jogador == 1:  # jogador jogou papel
                print('Infelizmente voce perdeu :( ')
            else:  # jogador jogou tesoura
                print('Empate entre voce e o computador. ')
else:
    print('Voce escolheu uma opção incorreta!')