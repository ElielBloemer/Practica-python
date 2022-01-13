frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) # O join junta as palavras
#inverso = ''
inverso = junto[::-1] # fatiamento
#for letra in range(len(junto)-1,-1,-1): USANDO O FOR
#    inverso+= junto[letra]
if inverso==junto:
        print(junto, inverso)
        print(' A frase É palindrome')
else:
        print(junto, inverso)
        print(' A frase NÃO palindrome ')
