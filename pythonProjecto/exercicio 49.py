num = int(input('Digite o numero que deseja ver a tabuada :'))
print('{:=^40} '.format(' TABUADA '))
for cont in range(0,11):
    print(' {} X {} = {} '.format(cont,num,cont*num))
