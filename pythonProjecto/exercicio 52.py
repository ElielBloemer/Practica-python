num = int(input('Digite um numero : '))
c=0
for cont in range(1,(num+1)):
    if num%cont==0:
        print('\033[031m',end=' ')# entro para pegar a cor que quero ler
        c+=1
    else:
        print('\033[033m',end=' ') # desfazo a cor que nao quero ler
    print('{}'.format(cont),end=' ')# mando ler o numero
if c==2:
    print('\n\033[mO numero {} É primo'.format(num))
else:
    print('\n\033[mO numero {} NÃo é primo'.format(num))