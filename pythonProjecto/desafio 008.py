#escreva um programa que leia um valor em metros  e o exiba convertendo em centímetros e milímetros
#2 metros = 200 centímetros.
#2 metros = 2000 milímetros.
n = float(input(' digite a quantidade de metros a converter :'))
print('{:.0f} metros é \n{:.0f} centimetros  \n{:.0f} milimitros. '.format(n,n*100,n*1000))
