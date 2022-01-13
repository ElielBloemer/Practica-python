# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro numero :'))
num2 = int(input('Digite o segundo numero :'))
num3 = int(input('Digite o terceiro numero :'))
if num1 > num2 and num1 > num3:
    if num2 < num3:
        print(' O número maior é {} e o menor é {}'.format(num1, num2))
    else:
        print(' O número maior é {} e o menor é {}'.format(num1, num3))
elif num2 > num1 and num2 > num3:
    if num1 < num3:
        print(' O número maior é {} e o menor é {}'.format(num2, num1))
    else:
        print(' O número maior é {} e o menor é {}'.format(num2, num3))
else:
    if num1 < num2:
        print(' O número maior é {} e o menor é {}'.format(num3, num1))
    else:
        print(' O número maior é {} e o menor é {}'.format(num3, num2))
