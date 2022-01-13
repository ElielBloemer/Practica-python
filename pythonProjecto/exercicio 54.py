'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
pessoaMaioridade = 0
pessoaMenorIdade = 0
for edad in range(0,7):
    ano = int(input('Digite o ano de nascimento da primera pessoa {} :'.format(edad+1)))
    if(2021-ano) >=18:
        pessoaMaioridade+=1
    else:
        pessoaMenorIdade+=1
print('Voce tem {} pessoas maior de idade e {} pessoas menor de idade'.format(pessoaMaioridade,pessoaMenorIdade),end=' FIN')
