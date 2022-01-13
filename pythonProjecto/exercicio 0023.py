'''faça um programa que leia um numero,
  de 0 a 9999 e mostre na tela cada um dos dígitos separados. exemplo : 1834.'''
num = int(input(' digite um numero '))
u = num % 10
d = int((num % 100) / 10)
c = int((num % 1000) / 100)
m = int(num / 1000)
print('  unidade  {}'.format(u))
print('  dezena  {}'.format(d))
print(' centena {}'.format(c))
print(' milhar {} '.format(m))
