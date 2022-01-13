print('='*40)
print(' 10 TERMOS DE UMA PROGRESSÃO ARTIMETICA')
print('='*40)
inicio = int(input('Digite o inicio : '))
razao = int(input('Digite a razão :'))
fim = razao*10
for c in range (inicio,fim,razao):
    print('{}'.format(c),end='-> ')
print(' FIM ')
