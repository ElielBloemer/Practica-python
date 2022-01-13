nome=str(input(' digite o nome ')).strip()#explicito que estou lendo ums string, e com o strip elimino os espacos dos lados
print(' analizando seu nome...')
print(' seu nome é com letras maiúsculas é {} \n e con letras minusculas é {}'.format(nome.upper(),nome.lower()), )
print(' seu nome tem {} letras '.format(len(nome)-nome.count(' ')))# conto o espacos total do nome - o espaço do meio
#print(' seu primeiro nome tem {} letras '.format(nome.find(' ')))
#outro possivel jeito
separador = nome.split()
print(' seu nome primeiro nome é {} e tem {} letras '.format(separador[0],len(separador[0]))) # pego a lista e mostro o primero da lista
# e agora conto o elemento 0 da lista

