n = input('DIGITE ALGO :')
print('O TIPO PRIMITIVO DESSE VALOR É {}' .format(type(n)))
print('só tem espaços ? {}'.format( n.isspace()))
print('é un numero? {}'.format(n.isnumeric()))
print('é alfanumerico? {}'.format( n.isalpha()))
print('esta en maiuscula? {}'.format(n.isupper()))
print('esta en minuscula?  '.format(n.islower()))
print('é alfanumérico? '.format( n.isalnum()))
print('esta capitalizada ? {}'.format(n.istitle()))# significa se a palavra tem maiusculas e minusculas ao mesmo tempo
